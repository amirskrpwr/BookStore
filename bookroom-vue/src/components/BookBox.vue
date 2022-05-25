<template>
  <div class="col-lg-3 col-md-6 mb-3">
    <div class="box-element">
      <router-link
        class="text-decoration-none"
        v-bind:to="book.get_absolute_url"
      >
        <img class="thumbnail" :src="book.get_image" :alt="book.image" />
        <h5 class="p-2 text-black-50 short">{{ book.name }}</h5>
        <h6 v-if="book.discount != 0" class="p-2 text-black-50">
          <span class="me-3">
            {{
              numberByCommas(parseInt(book.price * (1 - book.discount / 100)))
            }}
          </span>
          <span class="text-decoration-line-through text-danger">{{
            numberByCommas(parseInt(book.price))
          }}</span>
          تومان
        </h6>
        <h6 v-else class="p-2 text-black-50">
          {{ numberByCommas(parseInt(book.price)) }} تومان
        </h6>
      </router-link>
      <button
        class="btn btn-outline-secondary update-cart"
        @click="addToCart(book)"
      >
        افزودن به سبد خرید
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "BookBox",
  props: {
    book: Object,
  },
  methods: {
    addToCart(book) {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        book: book,
        quantity: this.quantity,
      };

      this.$store.commit("addToCart", item);
    },

    numberByCommas(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
  },
};
</script>

<style scoped>
.thumbnail {
  width: 100%;
  height: 250px;
}

.box-element {
  box-shadow: hsl(0, 0%, 80%) 0 0 16px;
  background-color: #fff;
  border-radius: 4px;
  padding: 10px;
}

.short {
  max-width: 250px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
</style>
