<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="box-element" id="form-wrapper">
        <form @submit.prevent="submitForm" class="p-2" action="" id="form">
          <div id="shipping-info">
            <h3>اطلاعات ارسال:</h3>
            <hr />

            <div class="form-field">
              <input
                type="text"
                placeholder="استان.."
                name="state"
                id="state"
                v-model="state"
                class="form-control"
              />
            </div>
            <div class="form-field">
              <input
                type="text"
                placeholder="شهر.."
                name="city"
                id="city"
                v-model="city"
                class="form-control"
              />
            </div>
            <div class="form-field">
              <input
                type="text"
                placeholder="نشانی.."
                name="address"
                id="address"
                v-model="address"
                class="form-control"
              />
            </div>
          </div>
          <hr />
          <input
            type="submit"
            class="btn btn-success"
            id="form-button"
            value="Continue"
          />
        </form>

        <div class="p-3 mb-2 bg-danger text-white" v-if="errors.length">
          <p v-for="error in errors" :key="error.id">{{ error }}</p>
        </div>
      </div>
      <br />
    </div>
    <div class="col-lg-6">
      <div class="box-element">
        <div class="p-2">
          <router-link to="/cart" class="btn btn-outline-dark">
            بازگشت به سبد خرید
          </router-link>
          <hr />
          <h3>خلاصه سفارش</h3>
          <hr />
          <div class="cart-row">
            <div style="flex: 2"></div>
            <div style="flex: 2"><strong>عنوان</strong></div>
            <div style="flex: 1.75"><strong>قیمت</strong></div>
            <div style="flex: 0.5"><strong>تعداد</strong></div>
          </div>
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
            <div style="flex: 2" class="align-self-center">
              <p>{{ item.book.name }}</p>
            </div>
            <div style="flex: 1.75" class="align-self-center">
              <p>{{ numberByCommas(parseInt(item.book.price)) }} تومان</p>
            </div>
            <div style="flex: 0.5" class="align-self-center">
              <p>{{ item.quantity }}</p>
            </div>
          </div>
          <div class="row">
            <h6 style="flex: 1">
              <strong>تعداد کتاب ها: </strong>
            </h6>
            <h6 style="flex: 2">{{ numberByCommas(getTotalCount) }} کتاب</h6>
          </div>
          <div class="row" v-if="getTotalDiscount">
            <h6 style="flex: 1">
              <strong>مجموع: </strong>
            </h6>
            <h6 style="flex: 2">{{ numberByCommas(getTotalAmount) }} تومان</h6>
          </div>
          <div class="row" v-if="getTotalDiscount">
            <h6 style="flex: 1">
              <strong>مجموع تخفیف: </strong>
            </h6>
            <h6 style="flex: 2" class="text-success">
              {{ numberByCommas(getTotalDiscount) }} تومان
            </h6>
          </div>
          <div class="row">
            <h6 style="flex: 1">
              <strong>مجموع قابل پرداخت: </strong>
            </h6>
            <h6 style="flex: 2">
              {{ numberByCommas(getTotalAmount - getTotalDiscount) }} تومان
            </h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "checkout",
  data() {
    return {
      cart: { items: [] },
      state: "",
      city: "",
      address: "",
      errors: [],
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
    getTotalDiscount() {
      let total = 0;
      for (let i = 0; i < this.cart.items.length; i++) {
        total +=
          ((this.cart.items[i].quantity * this.cart.items[i].book.discount) /
            100) *
          this.cart.items[i].book.price;
      }
      return total;
    },
  },
  methods: {
    numberByCommas(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },

    async submitForm() {
      this.errors = [];

      if (this.state === "") {
        this.errors.push("The state is missing.");
      }

      if (this.city === "") {
        this.errors.push("The city is missing.");
      }
      if (this.address === "") {
        this.errors.push("The address is missing.");
      }

      const data = {
        complete: true,
        orderItems: this.cart.items,
        state: this.state,
        city: this.city,
        address: this.address,
      };

      if (!this.errors.length) {
        this.$store.commit("setIsLoading", true);

        await axios
          .post("api/v1/checkout/", data)
          .then((res) => {
            this.$store.commit("clearCart");
            this.$router.push("/cart/success");
          })
          .catch((err) => {
            this.errors.push("something went wrong. please try again.");
            console.log(err);
          });

        this.$store.commit("setIsLoading", false);
      }
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
