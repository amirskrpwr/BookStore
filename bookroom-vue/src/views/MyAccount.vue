<template>
  <div>
    <div class="row">
      <div class="col-lg-3">
        <img
          v-if="customer.get_image"
          :src="customer.get_image"
          class="img-thumbnail"
          width="200"
          height="150"
          :alt="username"
        />
        <img
          v-else
          src="../assets/images/default.png"
          class="img-thumbnail"
          width="230"
          :alt="username"
        />
        <h1 class="mt-3">{{ username }}</h1>
        <div class="mt-3">
          <button
            class="btn btn-danger mb-3"
            data-bs-toggle="modal"
            data-bs-target="#demo"
          >
            خروج از حساب
          </button>
        </div>
      </div>
      <div class="col-lg-9">
        <button class="btn btn-success mb-3" @click="clickFadeModification()">
          ویرایش اطلاعات
        </button>
        <div id="fadeDivModification">
          <form
            @submit.prevent="postModification()"
            class="p-2"
            action=""
            id="form"
          >
            <div>
              <div class="row">
                <div class="col-lg-6">
                  <input
                    type="text"
                    placeholder="نام.."
                    name="last_name"
                    id="last_name"
                    v-model="customer.first_name"
                    class="form-control mb-2"
                  />
                </div>
                <div class="col-lg-6">
                  <input
                    type="text"
                    placeholder="نام خانوادگی.."
                    name="last_name"
                    id="last_name"
                    v-model="customer.last_name"
                    class="form-control mb-2"
                  />
                </div>
                <div class="col-lg-6 mb-2 align-self-stretch">
                  <birth-date-picker
                    v-model="customer.birth_date"
                  ></birth-date-picker>
                </div>
                <div class="col-lg-6 mb-2 align-self-stretch">
                  <input
                    type="file"
                    name="image"
                    placeholder="عکس پروفایل را انتخاب کنید"
                    id="image"
                    v-on:change="onFileSelected"
                    accept="image/png, image/gif, image/jpeg, image/jpg"
                    class="form-control mb-2 text-lowercase"
                  />
                </div>
              </div>
            </div>

            <button type="submit" class="btn btn-success mt-3">
              ثبت اطلاعات
            </button>
          </form>
          <hr />

          <div v-if="email">
            <h3 class="text-lowercase">
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
                class="form-control text-lowercase"
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
          <br />
        </div>
      </div>
    </div>

    <div v-show="orders.length">
      <hr />
      <h2>سفارشات:</h2>
      <br />
      <div v-for="index in orders.length" :key="orders[index - 1].id">
        <div class="box-element">
          <div class="cart-row">
            <div style="flex: 1.5"></div>
            <div style="flex: 2" class="ms-4"><strong>عنوان</strong></div>
            <div style="flex: 1.2" class="ms-2"><strong>قیمت</strong></div>
            <div style="flex: 0.5" class="ms-2"><strong>تعداد</strong></div>
            <div style="flex: 0.9" class="ms-2"><strong>جمع کل</strong></div>
          </div>
          <span></span>
          <div
            v-for="item in orders[index - 1].orderItems"
            :key="item.id"
            class="cart-row"
          >
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
              <p>{{ toFarsiNumber(item.book.name) }}</p>
            </div>
            <div style="flex: 1.2" class="align-self-center ms-2">
              <p v-if="item.discount != 0">
                <span class="me-2">
                  {{
                    toFarsiNumber(
                      numberByCommas(
                        parseInt(item.price * (1 - item.discount / 100))
                      )
                    )
                  }}
                </span>
                <span class="text-decoration-line-through text-danger">{{
                  toFarsiNumber(numberByCommas(parseInt(item.price)))
                }}</span>
                تومان
              </p>
              <p v-else>
                {{ toFarsiNumber(numberByCommas(parseInt(item.price))) }}
                تومان
              </p>
            </div>
            <div style="flex: 0.5" class="align-self-center ms-2">
              <p>{{ item.quantity }}</p>
            </div>
            <div style="flex: 0.9" class="align-self-center ms-2">
              <p>
                {{
                  toFarsiNumber(
                    numberByCommas(
                      item.price * item.quantity * (1 - item.discount / 100)
                    )
                  )
                }}
                تومان
              </p>
            </div>
          </div>
          <div class="row pt-3 pb-3">
            <div style="flex: 1"><strong>جمع کل: </strong></div>
            <div style="flex: 7">
              {{
                toFarsiNumber(numberByCommas(getOrderTotal.split("*")[index]))
              }}
              تومان
            </div>
          </div>
          <div class="row pt-3 pb-3">
            <div style="flex: 1"><strong>محل ارسال: </strong></div>
            <div style="flex: 4">
              {{ orders[index - 1].state }}، {{ orders[index - 1].city }}،
              {{ toFarsiNumber(orders[index - 1].address) }}
            </div>
            <div style="flex: 1"><strong>زمان سفارش: </strong></div>
            <div style="flex: 2">
              {{ toFarsiNumber(getPersianDate(orders[index - 1].date_added)) }}
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
import Toastify from "toastify-js";
import axios from "axios";

export default {
  name: "MyAccount",
  data() {
    return {
      username: "",
      password: "",
      customer: {},
      selectedImage: "",
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
  computed: {
    getOrderTotal() {
      let total = "";
      for (let order of this.orders) {
        let sum = 0;
        for (let item of order.orderItems) {
          sum += item.quantity * ((item.price * (100 - item.discount)) / 100);
        }
        total += "*" + sum;
      }
      return total;
    },
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");
      localStorage.removeItem("username");
      localStorage.removeItem("userid");

      this.$store.commit("clearCart");
      this.$store.commit("removeToken");

      Toastify({
        text: "خروج از حساب با موفقیت انجام شد.",
        duration: 3000,
        newWindow: true,
        gravity: "bottom",
        position: "right",
        stopOnFocus: true,
        style: {
          background: "#5cdb95",
        },
      }).showToast();

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

          axios
            .get(`api/v1/customers/${this.id}`)
            .then((res) => {
              this.customer = res.data;
              this.customer.birth_date =
                res.data.birth_date === "1000-01-01" ? null : birth_date;
              console.log(res.data);
            })
            .catch((err) => console.log(err));
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

      if (!this.newEmail)
        Toastify({
          text: "ایمیل وارد نشده است.",
          duration: 3000,
          newWindow: true,
          gravity: "bottom",
          position: "right",
          stopOnFocus: true,
          style: {
            background: "#ff652f",
          },
        }).showToast();
      else
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

            Toastify({
              text: "ایمیل با موفقیت تغییر یافت",
              duration: 3000,
              newWindow: true,
              gravity: "bottom",
              position: "right",
              stopOnFocus: true,
              style: {
                background: "#5cdb95",
              },
            }).showToast();

            this.clickFade();
          })
          .catch((err) => {
            console.log(err);

            Toastify({
              text: "مشکلی در تغییر ایمیل به وجود آمد.",
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
    },
    async postModification() {
      this.$store.commit("setIsLoading", true);
      const formData = new FormData();
      this.selectedImage
        ? formData.append("image", this.selectedImage, this.selectedImage.name)
        : null;
      formData.append(
        "first_name",
        this.customer.first_name ? this.customer.first_name : ""
      );
      formData.append(
        "last_name",
        this.customer.last_name ? this.customer.last_name : ""
      );
      formData.append("user", this.id);
      formData.append(
        "birth_date",
        this.customer.birth_date ? this.customer.birth_date : "1000-01-01"
      );
      await axios
        .post("api/v1/customers/", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        })
        .then((res) => {
          Toastify({
            text: "اطلاعات با موفقیت ارسال شد.",
            duration: 3000,
            newWindow: true,
            gravity: "bottom",
            position: "right",
            stopOnFocus: true,
            style: {
              background: "#5cdb95",
            },
          }).showToast();
          location.reload();
          this.clickFadeModification();
        })
        .catch((err) => {
          console.log(err);

          if (err.response.status === 500) {
            Toastify({
              text: "اطلاعات با موفقیت ارسال شد.",
              duration: 3000,
              newWindow: true,
              gravity: "bottom",
              position: "right",
              stopOnFocus: true,
              style: {
                background: "#5cdb95",
              },
            }).showToast();
            location.reload();
          } else {
            Toastify({
              text: "مشکلی در ارسال اطلاعات بوجود آمد.",
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

          this.clickFadeModification();
        });

      this.$store.commit("setIsLoading", false);
    },
    numberByCommas(number) {
      return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    onFileSelected(e) {
      this.selectedImage = e.target.files[0];
    },
    clickFade() {
      document.getElementById("fadeDiv").classList.toggle("fade");
    },
    clickFadeModification() {
      document.getElementById("fadeDivModification").classList.toggle("fade");
    },
    getPersianDate(date) {
      let week = new Array(
        "يكشنبه",
        "دوشنبه",
        "سه شنبه",
        "چهارشنبه",
        "پنج شنبه",
        "جمعه",
        "شنبه"
      );
      let months = new Array(
        "فروردين",
        "ارديبهشت",
        "خرداد",
        "تير",
        "مرداد",
        "شهريور",
        "مهر",
        "آبان",
        "آذر",
        "دي",
        "بهمن",
        "اسفند"
      );
      let dateDay = new Date(date);
      let d = dateDay.getDay();
      let day = dateDay.getDate();
      let month = dateDay.getMonth() + 1;
      let year = dateDay.getYear();
      let hours = dateDay.getHours();
      let minutes = dateDay.getMinutes();
      let seconds = dateDay.getSeconds();
      year =
        window.navigator.userAgent.indexOf("MSIE") > 0 ? year : 1900 + year;
      if (year == 0) {
        year = 2000;
      }
      if (year < 100) {
        year += 1900;
      }
      let y = 1;
      for (let i = 0; i < 3000; i += 4) {
        if (year == i) {
          y = 2;
        }
      }
      for (let i = 1; i < 3000; i += 4) {
        if (year == i) {
          y = 3;
        }
      }
      if (y == 1) {
        year -= month < 3 || (month == 3 && day < 21) ? 622 : 621;
        switch (month) {
          case 1:
            day < 21
              ? ((month = 10), (day += 10))
              : ((month = 11), (day -= 20));
            break;
          case 2:
            day < 20
              ? ((month = 11), (day += 11))
              : ((month = 12), (day -= 19));
            break;
          case 3:
            day < 21 ? ((month = 12), (day += 9)) : ((month = 1), (day -= 20));
            break;
          case 4:
            day < 21 ? ((month = 1), (day += 11)) : ((month = 2), (day -= 20));
            break;
          case 5:
          case 6:
            day < 22
              ? ((month -= 3), (day += 10))
              : ((month -= 2), (day -= 21));
            break;
          case 7:
          case 8:
          case 9:
            day < 23 ? ((month -= 3), (day += 9)) : ((month -= 2), (day -= 22));
            break;
          case 10:
            day < 23 ? ((month = 7), (day += 8)) : ((month = 8), (day -= 22));
            break;
          case 11:
          case 12:
            day < 22 ? ((month -= 3), (day += 9)) : ((month -= 2), (day -= 21));
            break;
          default:
            break;
        }
      }
      if (y == 2) {
        year -= month < 3 || (month == 3 && day < 20) ? 622 : 621;
        switch (month) {
          case 1:
            day < 21
              ? ((month = 10), (day += 10))
              : ((month = 11), (day -= 20));
            break;
          case 2:
            day < 20
              ? ((month = 11), (day += 11))
              : ((month = 12), (day -= 19));
            break;
          case 3:
            day < 20 ? ((month = 12), (day += 10)) : ((month = 1), (day -= 19));
            break;
          case 4:
            day < 20 ? ((month = 1), (day += 12)) : ((month = 2), (day -= 19));
            break;
          case 5:
            day < 21 ? ((month = 2), (day += 11)) : ((month = 3), (day -= 20));
            break;
          case 6:
            day < 21 ? ((month = 3), (day += 11)) : ((month = 4), (day -= 20));
            break;
          case 7:
            day < 22 ? ((month = 4), (day += 10)) : ((month = 5), (day -= 21));
            break;
          case 8:
            day < 22 ? ((month = 5), (day += 10)) : ((month = 6), (day -= 21));
            break;
          case 9:
            day < 22 ? ((month = 6), (day += 10)) : ((month = 7), (day -= 21));
            break;
          case 10:
            day < 22 ? ((month = 7), (day += 9)) : ((month = 8), (day -= 21));
            break;
          case 11:
            day < 21 ? ((month = 8), (day += 10)) : ((month = 9), (day -= 20));
            break;
          case 12:
            day < 21 ? ((month = 9), (day += 10)) : ((month = 10), (day -= 20));
            break;
          default:
            break;
        }
      }
      if (y == 3) {
        year -= month < 3 || (month == 3 && day < 21) ? 622 : 621;
        switch (month) {
          case 1:
            day < 20
              ? ((month = 10), (day += 11))
              : ((month = 11), (day -= 19));
            break;
          case 2:
            day < 19
              ? ((month = 11), (day += 12))
              : ((month = 12), (day -= 18));
            break;
          case 3:
            day < 21 ? ((month = 12), (day += 10)) : ((month = 1), (day -= 20));
            break;
          case 4:
            day < 21 ? ((month = 1), (day += 11)) : ((month = 2), (day -= 20));
            break;
          case 5:
          case 6:
            day < 22
              ? ((month -= 3), (day += 10))
              : ((month -= 2), (day -= 21));
            break;
          case 7:
          case 8:
          case 9:
            day < 23 ? ((month -= 3), (day += 9)) : ((month -= 2), (day -= 22));
            break;
          case 10:
            day < 23 ? ((month = 7), (day += 8)) : ((month = 8), (day -= 22));
            break;
          case 11:
          case 12:
            day < 22 ? ((month -= 3), (day += 9)) : ((month -= 2), (day -= 21));
            break;
          default:
            break;
        }
      }
      if (hours < 10) hours = "0" + hours;
      if (minutes < 10) minutes = "0" + minutes;
      if (seconds < 10) seconds = "0" + seconds;
      return `${week[d]} ${day} ${
        months[month - 1]
      } ${year}، ${hours}:${minutes}:${seconds} `;
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

#fadeDiv {
  display: none;
  opacity: 0;
  transition: opacity 0.4s ease-in-out;
}

#fadeDiv.fade {
  display: block;
  opacity: 1;
}
#fadeDivModification {
  display: none;
  opacity: 0;
  transition: opacity 0.4s ease-in-out;
}

#fadeDivModification.fade {
  display: block;
  opacity: 1;
}

text-transform {
  text-transform: lowercase;
}
</style>
