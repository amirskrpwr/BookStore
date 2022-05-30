<template>
  <div>
    <div>
      <h1>{{ username }}</h1>
      <div v-if="email">
        <h3>
          {{ email }}
          <button class="btn btn-primary" @click="clickFade()">
            تغییر ایمیل
          </button>
        </h3>
      </div>
      <div v-else>
        <button class="btn btn-warning" @click="clickFade()">
          افزودن ایمیل
        </button>
      </div>
      <div id="fadeDiv">
        <form
          @submit.prevent="postEmail()"
          style="width: 60%"
          class="d-flex mt-3"
        >
          <input
            class="form-control"
            name="email"
            type="email"
            v-model="newEmail"
            placeholder="ایمیل خود را وارد نمائید.."
          />
          <button class="btn btn-outline-success me-2" type="submit">
            ثبت ایمیل
          </button>
        </form>
      </div>
      <br />
      <div>
        <button
          class="btn btn-danger"
          data-bs-toggle="modal"
          data-bs-target="#demo"
        >
          خروج از حساب
        </button>
      </div>
    </div>
    <div v-show="orders.length">
      <hr />
      <h2>سفارشات:</h2>
      <br />
      <div v-for="order in orders" :key="order.id">
        <div class="box-element">
          <div class="cart-row">
            <div style="flex: 1.5"></div>
            <div style="flex: 2" class="ms-4"><strong>عنوان</strong></div>
            <div style="flex: 1.2" class="ms-2"><strong>قیمت</strong></div>
            <div style="flex: 0.5" class="ms-2"><strong>تعداد</strong></div>
            <div style="flex: 0.9" class="ms-2"><strong>جمع کل</strong></div>
          </div>
          <span></span>
          <div v-for="item in order.orderItems" :key="item.id" class="cart-row">
            <div style="flex: 1.5" class="align-self-center">
              <router-link :to="item.book.get_absolute_url">
                <img
                  :src="item.book.get_image"
                  :alt="item.book.name"
                  class="row-image"
                />
              </router-link>
            </div>
            <div style="flex: 2" class="align-self-center ms-4">
              <p>{{ item.book.name }}</p>
            </div>
            <div style="flex: 1.2" class="align-self-center ms-2">
              <p v-if="item.book.discount != 0">
                <span class="me-2">
                  {{
                    numberByCommas(
                      parseInt(item.book.price * (1 - item.book.discount / 100))
                    )
                  }}
                </span>
                <span class="text-decoration-line-through text-danger">{{
                  numberByCommas(parseInt(item.book.price))
                }}</span>
                تومان
              </p>
              <p v-else>
                {{ numberByCommas(parseInt(item.book.price)) }} تومان
              </p>
            </div>
            <div
              style="flex: 0.5"
              class="align-self-center d-flex justify-content-center ms-2"
            >
              <p>{{ item.quantity }}</p>
            </div>
            <div style="flex: 0.9" class="align-self-center ms-2">
              <p>
                {{
                  numberByCommas(
                    item.book.price *
                      item.quantity *
                      (1 - item.book.discount / 100)
                  )
                }}
                تومان
              </p>
            </div>
          </div>
          <div class="row pt-3 pb-3">
            <div style="flex: 1"><strong>محل ارسال: </strong></div>
            <div style="flex: 4">
              {{ order.state }}، {{ order.city }}، {{ order.address }}
            </div>
          </div>
        </div>
        <br />
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
            <h5 class="modal-title" id="exampleModalLabel">خروج از حساب</h5>
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
            آیا می‌خواهید از حساب کاربریتان خارج شوید؟
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
              @click="logout()"
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
  name: "MyAccount",
  data() {
    return {
      username: "",
      password: "",
      email: "",
      newEmail: "",
      id: "",
      orders: [],
    };
  },
  mounted() {
    this.username = this.$store.state.username;
    this.password = this.$store.state.password;
    document.title = "Account | BookStore";
    this.getUserInfo();
    this.getMyOrders();
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");

      this.$store.commit("removeToken");

      this.$router.push("/");
    },
    async getUserInfo() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("api/v1/users/me", {
          auth: {
            username: this.username,
            password: this.password,
          },
        })
        .then((res) => {
          this.id = res.data.id;
          this.email = res.data.email;
          console.log("data: ", res.data);
        })
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
    async getMyOrders() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("api/v1/orders/")
        .then((res) => {
          this.orders = res.data;
        })
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
    async postEmail() {
      this.$store.commit("setIsLoading", true);

      await axios
        .put(
          "api/v1/users/me/",
          {
            email: this.newEmail,
          },
          {
            auth: {
              username: this.username,
              password: this.password,
            },
          }
        )
        .then((res) => {
          this.email = this.newEmail;
          this.newEmail = "";
          this.$router.push("/my-account");
        })
        .catch((err) => {
          this.errors.push("something went wrong. please try again.");
          console.log(err);
        });

      this.$store.commit("setIsLoading", false);
    },
    numberByCommas(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },

    clickFade() {
      document.getElementById("fadeDiv").classList.toggle("fade");
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

#fadeDiv {
  display: none;
  opacity: 0;
  transition: opacity 0.4s ease-in-out;
}

#fadeDiv.fade {
  display: block;
  opacity: 1;
}
</style>
