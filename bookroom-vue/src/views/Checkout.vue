<template>
  <div class="row">
    <div class="col-lg-6">
      <div class="box-element" id="form-wrapper">
        <form @submit.prevent="showButton" class="p-2" action="" id="form">
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

          <button type="submit" class="btn btn-success" id="form-button">
            ادامه
          </button>
        </form>
      </div>
      <br />
      <div
        class="box-element d-flex justify-content-center hidden"
        id="complete"
      >
        <button
          class="btn btn-success"
          data-bs-toggle="modal"
          data-bs-target="#demo"
        >
          تکمیل خرید
        </button>
      </div>
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
            <div style="flex: 2" class="ms-4"><strong>عنوان</strong></div>
            <div style="flex: 1.75" class="ms-2"><strong>قیمت</strong></div>
            <div style="flex: 0.5" class="ms-2"><strong>تعداد</strong></div>
          </div>
          <div v-for="item in cart.items" :key="item.id" class="cart-row">
            <div style="flex: 2" class="align-self-center">
              <router-link :to="item.book.get_absolute_url">
                <img
                  :src="item.book.get_image"
                  :alt="toFarsiNumber(item.book.name)"
                  class="row-image short"
                />
              </router-link>
            </div>
            <div style="flex: 2" class="align-self-center ms-4">
              <p>{{ toFarsiNumber(item.book.name) }}</p>
            </div>
            <div style="flex: 1.75" class="align-self-center ms-2">
              <p>
                {{ toFarsiNumber(numberByCommas(parseInt(item.book.price))) }}
                تومان
              </p>
            </div>
            <div style="flex: 0.5" class="align-self-center ms-2">
              <p>{{ toFarsiNumber(item.quantity) }}</p>
            </div>
          </div>
          <div class="row">
            <h6 style="flex: 1">
              <strong>تعداد کتاب ها: </strong>
            </h6>
            <h6 style="flex: 2">{{ toFarsiNumber(getTotalCount) }} کتاب</h6>
          </div>
          <div class="row" v-if="getTotalDiscount">
            <h6 style="flex: 1">
              <strong>مجموع: </strong>
            </h6>
            <h6 style="flex: 2">
              {{ toFarsiNumber(numberByCommas(getTotalAmount)) }} تومان
            </h6>
          </div>
          <div class="row" v-if="getTotalDiscount">
            <h6 style="flex: 1">
              <strong>مجموع تخفیف: </strong>
            </h6>
            <h6 style="flex: 2" class="text-success">
              {{ toFarsiNumber(numberByCommas(getTotalDiscount)) }} تومان
            </h6>
          </div>
          <div class="row">
            <h6 style="flex: 1">
              <strong>مجموع قابل پرداخت: </strong>
            </h6>
            <h6 style="flex: 2">
              {{
                toFarsiNumber(numberByCommas(getTotalAmount - getTotalDiscount))
              }}
              تومان
            </h6>
          </div>
        </div>
      </div>
    </div>

    <!-- modal -->
    <div
      class="modal fade"
      id="demo"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">نهایی کردن خرید</h5>
            <div class="d-flex flex-row-reverse">
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
          </div>
          <div class="modal-body">
            آیا می‌خواهید این {{ toFarsiNumber(getTotalCount) }} کتاب را با
            مجموع {{ toFarsiNumber(numberByCommas(getTotalAmount)) }} تومان
            خریداری کنید؟
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              خیر
            </button>
            <button
              type="button"
              @click="submitForm"
              class="btn btn-primary"
              data-bs-dismiss="modal"
            >
              بله
            </button>
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

    showButton() {
      this.errors = [];

      if (this.state === "") {
        this.errors.push("فیلد استان وارد نشده‌ است.");

        Toastify({
          text: "فیلد استان وارد نشده‌ است.",
          duration: 3000,
          newWindow: true,
          gravity: "bottom",
          position: "right",
          stopOnFocus: true,
          style: {
            background: "#ff652f",
          },
        }).showToast();
      }

      if (this.city === "") {
        this.errors.push("فیلد شهر وارد نشده‌ است.");

        Toastify({
          text: "فیلد شهر وارد نشده‌ است.",
          duration: 3000,
          newWindow: true,
          gravity: "bottom",
          position: "right",
          stopOnFocus: true,
          style: {
            background: "#ff652f",
          },
        }).showToast();
      }
      if (this.address === "") {
        this.errors.push("فیلد آدرس وارد نشده‌ است.");

        Toastify({
          text: "فیلد آدرس وارد نشده است.",
          duration: 3000,
          newWindow: true,
          gravity: "bottom",
          position: "right",
          stopOnFocus: true,
          style: {
            background: "#ff652f",
          },
        }).showToast();
      }
      if (!this.errors.length)
        document.getElementById("complete").classList.remove("hidden");
    },

    async submitForm() {
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

            Toastify({
              text: "خرید شما با موفقیت صورت گرفت.",
              duration: 3000,
              newWindow: true,
              gravity: "bottom",
              position: "right",
              stopOnFocus: true,
              style: {
                background: "#5cdb95",
              },
            }).showToast();

            this.$router.push("/cart/success");
          })
          .catch((err) => {
            this.errors.push("something went wrong. please try again.");
            console.log(err);

            Toastify({
              text: "مشکلی در عملیات خرید پیش آمد لطفا دوباره امتحان کنید.",
              duration: 3000,
              newWindow: true,
              gravity: "bottom",
              position: "right",
              stopOnFocus: true,
              style: {
                background: "#ff652f",
              },
            }).showToast();
          });

        this.$store.commit("setIsLoading", false);
      }
    },

    toFarsiNumber(n) {
      const farsiDigits = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"];

      return n.toString().replace(/\d/g, (x) => farsiDigits[x]);
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
