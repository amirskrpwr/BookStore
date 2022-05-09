<template>
  <div class="row" v-if="getTotalCount">
    <div class="col-lg-12">
      <div class="box-element">
        <router-link to="/" class="btn btn-outline-dark">
          &#x2190; Continue Shopping
        </router-link>
        <br /><br />
        <table class="table">
          <th>
            <h5>
              Items: <strong>{{ numberByCommas(getTotalCount) }}</strong>
            </h5>
          </th>
          <th>
            <h5>
              Total:
              <strong>$ {{ numberByCommas(getTotalAmount) }}</strong>
            </h5>
          </th>
          <th>
            <router-link
              to="/cart/checkout"
              class="btn btn-success"
              v-if="getTotalCount"
              id="btn-checkout"
            >
              Checkout
            </router-link>
          </th>
        </table>
      </div>
      <br />
      <div class="box-element">
        <div class="cart-row">
          <div style="flex: 1.5"></div>
          <div style="flex: 1.5"><strong>Item</strong></div>
          <div style="flex: 1"><strong>Price</strong></div>
          <div style="flex: 1"><strong>Quantity</strong></div>
          <div style="flex: 1"><strong>Total</strong></div>
          <div style="flex: 0.6"></div>
        </div>
        <span></span>
        <div v-for="item in cart.items" :key="item.id" class="cart-row">
          <div style="flex: 1.5">
            <router-link :to="item.book.get_absolute_url">
              <img
                :src="item.book.get_image"
                :alt="item.book.name"
                class="row-image"
              />
            </router-link>
          </div>
          <div style="flex: 1.5">{{ item.book.name }}</div>
          <div style="flex: 1">
            ${{ numberByCommas(parseInt(item.book.price)) }}
          </div>
          <div style="flex: 1">
            <p class="quantity">{{ item.quantity }}</p>
            <div class="quantity">
              <img
                src="../assets/images/arrow-up.png"
                alt=""
                @click="incrementQuantity(item)"
                class="chg-quantity update-cart"
              />

              <img
                v-if="item.quantity > 1"
                src="../assets/images/arrow-down.png"
                alt=""
                @click="decrementQuantity(item)"
                class="chg-quantity update-cart"
              />
              <img
                v-else
                src="../assets/images/arrow-down.png"
                alt=""
                class="chg-quantity update-cart"
                data-bs-toggle="modal"
                :data-bs-target="'#demo' + item.book.id"
              />
            </div>
          </div>
          <div style="flex: 1">
            $ {{ numberByCommas(item.quantity * item.book.price) }}
          </div>
          <div style="flex: 0.6">
            <img
              src="../assets/images/trash.png"
              id="trash-icon"
              alt="trash"
              data-bs-toggle="modal"
              :data-bs-target="'#demo' + item.book.id"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- modal -->
    <div
      v-for="item in cart.items"
      :key="item.book.id"
      class="modal fade"
      v-bind:id="['demo' + item.book.id]"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">Are you sure?</div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              No
            </button>
            <button
              type="button"
              @click="removeItem(item)"
              class="btn btn-primary"
              data-bs-dismiss="modal"
            >
              Yes
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <h2>There is no book in the cart</h2>
  </div>
</template>

<script>
export default {
  name: "Cart",

  data() {
    return {
      cart: {
        items: [],
      },
    };
  },

  mounted() {
    document.title = "Cart | BookRoom";
    this.cart = this.$store.state.cart;
  },

  computed: {
    getTotalAmount() {
      let total = 0;
      for (let i = 0; i < this.cart.items.length; i++) {
        total += this.cart.items[i].quantity * this.cart.items[i].book.price;
      }
      return total;
    },
    getTotalCount() {
      let total = 0;
      for (let i = 0; i < this.cart.items.length; i++) {
        total += this.cart.items[i].quantity;
      }
      return total;
    },
  },

  methods: {
    incrementQuantity(item) {
      item.quantity += 1;

      this.updateCart();
    },
    decrementQuantity(item) {
      item.quantity -= 1;

      if (item.quantity === 0) {
        this.removeItem(item);
      }

      this.updateCart();
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
.box-element {
  box-shadow: hsl(0, 0%, 80%) 0 0 16px;
  background-color: #fff;
  border-radius: 4px;
  padding: 10px;
}

#btn-checkout {
  float: right;
  margin: 5px;
}

.cart-row {
  display: flex;
  align-items: flex-stretch;
  vertical-align: middle;
  padding-bottom: 10px;
  margin-bottom: 10px;
  border-bottom: 1px solid #ececec;
}

.quantity {
  display: inline-block;
  font-weight: 700;
  padding-right: 10px;
}

.chg-quantity {
  width: 12px;
  cursor: pointer;
  display: block;
  margin-top: 5px;
  transition: 0.1s;
}

.chg-quantity:hover {
  opacity: 0.6;
}

.row-image {
  width: 20%;
  margin-left: 25px;
}

#trash-icon {
  width: 25px;
  margin-left: 15px;
  display: inline-block;
  font-weight: 700;
  padding-right: 10px;
  cursor: pointer;
  transition: 0.1s;
}

#trash-icon:hover {
  opacity: 0.6;
}
</style>
