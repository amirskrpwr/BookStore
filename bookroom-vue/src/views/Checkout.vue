<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="box-element" id="form-wrapper">
        <form action="" id="form">
          <div id="user-info">
            <div class="form-info">
              <div class="form-field">
                <input
                  required
                  placeholder="name.."
                  type="text"
                  name="name"
                  id=""
                  class="form-control"
                />
              </div>
              <div class="form-field">
                <input
                  required
                  placeholder="email.."
                  type="email"
                  name="email"
                  id=""
                  class="form-control"
                />
              </div>
            </div>
          </div>
          <div id="shipping-info">
            <hr />
            <p>Shipping Infromation:</p>
            <hr />
            <div class="form-field">
              <input
                type="text"
                placeholder="Address.."
                name="address"
                id="address"
                class="form-control"
              />
            </div>
            <div class="form-field">
              <input
                type="text"
                placeholder="City.."
                name="city"
                id="city"
                class="form-control"
              />
            </div>
            <div class="form-field">
              <input
                type="text"
                placeholder="State.."
                name="state"
                id="state"
                class="form-control"
              />
            </div>
            <div class="form-field">
              <input
                type="text"
                placeholder="Zipcode.."
                name="zipcode"
                id="zipcode"
                class="form-control"
              />
            </div>
            <div class="form-field">
              <input
                type="text"
                placeholder="Country.."
                name="country"
                id="country"
                class="form-control"
              />
            </div>
          </div>
          <hr />
          <input
            type="submit"
            class="btn btn-success btn-block"
            id="form-button"
            value="Continue"
          />
        </form>
      </div>
      <br />
      <div class="box-element hidden" id="payment-info">
        <small>PayPal Options</small>
        <button id="make-payment">Make Payment</button>
      </div>
    </div>
    <div class="col-lg-6">
      <div class="box-element">
        <router-link to="/cart" class="btn btn-outline-dark">
          Back to cart
        </router-link>
        <hr />
        <h3>Order Summary</h3>
        <hr />
        <div v-for="item in cart.items" :key="item.id" class="cart-row">
          <div style="flex: 2">
            <router-link :to="item.book.get_absolute_url">
              <img
                :src="item.book.get_image"
                :alt="item.book.name"
                class="row-image"
              />
            </router-link>
          </div>
          <div style="flex: 2">
            <p>{{ item.book.name }}</p>
          </div>
          <div style="flex: 1">
            <p>
              ${{
                numberByCommas((item.book.price * item.quantity).toFixed(2))
              }}
            </p>
          </div>
          <div style="flex: 1">
            <p>x{{ item.quantity }}</p>
          </div>
        </div>
        <h5>Items: {{ numberByCommas(getTotalCount) }}</h5>
        <h5>Total: ${{ numberByCommas(getTotalAmount.toFixed(2)) }}</h5>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "checkout",
  data() {
    return {
      cart: { items: [] },
    };
  },
  mounted() {
    document.title = "Checkout | BookRoom";
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
    numberByCommas(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
  },
};
</script>

<style scoped>
.form-field {
  width: 250px;
  display: inline-block;
  padding: 5px;
}

.hidden {
  display: none !important;
}

.box-element {
  box-shadow: hsl(0, 0%, 80%) 0 0 16px;
  background-color: #fff;
  border-radius: 4px;
  padding: 10px;
}

.cart-row {
  display: flex;
  align-items: flex-stretch;
  padding-bottom: 10px;
  margin-bottom: 10px;
  border-bottom: 1px solid #ececec;
}

.row-image {
  width: 20%;
  margin-left: 25px;
}
</style>
