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
      <div class="d-flex justify-content-between">
        <div>
          <div v-if="book.count">
            <button
              v-if="
                !this.$store.state.cart.items.filter(
                  (item) => item.book.id === book.id
                ).length
              "
              class="btn btn-outline-secondary update-cart"
              @click="addToCart(book)"
            >
              افزودن کتاب
            </button>
            <div v-else>
              <button
                class="btn btn-success"
                @click="
                  incrementQuantity(
                    this.$store.state.cart.items.filter(
                      (item) => item.book.id === book.id
                    )[0]
                  )
                "
              >
                +
              </button>
              <span class="me-2 ms-2">
                {{
                  this.$store.state.cart.items.filter(
                    (item) => item.book.id === book.id
                  )[0].quantity
                }}
              </span>
              <button
                class="btn btn-success"
                @click="
                  decrementQuantity(
                    this.$store.state.cart.items.filter(
                      (item) => item.book.id === book.id
                    )[0]
                  )
                "
              >
                -
              </button>
            </div>
          </div>
          <div v-else>
            <button class="btn btn-secondary" disabled>موجود نیست</button>
          </div>
        </div>
        <div
          class="align-self-end p-1"
          v-if="book.count <= 5 && book.count > 0"
        >
          <small>تنها {{ book.count }} عدد باقیست</small>
        </div>
      </div>
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

    incrementQuantity(item) {
      if (item.quantity < item.book.count) {
        item.quantity += 1;
      }
      this.updateCart(item);
    },
    decrementQuantity(item) {
      item.quantity -= 1;

      if (item.quantity === 0) {
        this.removeItem(item);
      }

      this.updateCart(item);
    },

    removeItem(item) {
      this.$store.commit("removeFromCart", item);
    },

    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
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
