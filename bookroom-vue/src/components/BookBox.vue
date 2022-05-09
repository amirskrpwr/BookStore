<template>
  <div class="col-lg-3 col-md-6 mb-3">
    <div class="box-element">
      <img class="thumbnail" :src="book.get_image" :alt="book.image" />
      <h4 class="p-2">{{ book.name }}</h4>
      <h5>${{ numberByCommas(parseInt(book.price)) }}</h5>
      <button
        class="btn btn-outline-secondary update-cart"
        @click="addToCart(book)"
      >
        Add to cart
      </button>
      <router-link
        v-bind:to="book.get_absolute_url"
        class="btn btn-outline-secondary update-cart ms-2"
        >View Details</router-link
      >
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
</style>
