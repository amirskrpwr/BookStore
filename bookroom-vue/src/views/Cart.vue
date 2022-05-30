<template>
  <div>
    <div class="row" v-if="getTotalCount">
      <div class="col-lg-12">
        <div class="box-element">
          <router-link to="/" class="btn btn-outline-dark">
            &#x2190; بازگشت به خرید
          </router-link>
          <br /><br />
          <table class="table">
            <th>
              <h6>
                تعداد کتاب: <strong>{{ numberByCommas(getTotalCount) }}</strong>
              </h6>
            </th>
            <th>
              <h6>
                جمع کل:
                <strong>{{ numberByCommas(getTotalAmount) }} تومان</strong>
              </h6>
            </th>
            <th class="d-flex flex-row-reverse">
              <router-link
                to="/cart/checkout"
                class="btn btn-success"
                v-if="getTotalCount"
                id="btn-checkout"
              >
                پرداخت
              </router-link>
            </th>
          </table>
        </div>
        <br />
        <div class="box-element">
          <div class="cart-row">
            <div style="flex: 1.1"></div>
            <div class="ms-4" style="flex: 1.5"><strong>عنوان</strong></div>
            <div style="flex: 1"><strong>قیمت</strong></div>
            <div style="flex: 0.6"><strong>تعداد</strong></div>
            <div v-if="getTotalDiscount" style="flex: 0.7"></div>
            <div style="flex: 1"><strong>جمع کل</strong></div>
            <div style="flex: 0.2"></div>
          </div>
          <span></span>
          <div v-for="item in cart.items" :key="item.id" class="cart-row">
            <div style="flex: 1.1" class="align-self-center">
              <router-link :to="item.book.get_absolute_url">
                <img
                  :src="item.book.get_image"
                  :alt="item.book.name"
                  class="row-image"
                />
              </router-link>
            </div>
            <div style="flex: 1.5" class="align-self-center ms-4">
              {{ item.book.name }}
            </div>
            <div style="flex: 1" class="align-self-center ms-2">
              {{ numberByCommas(parseInt(item.book.price)) }} تومان
            </div>
            <div style="flex: 0.6" class="align-self-center ms-2">
              <p class="quantity">{{ item.quantity }}</p>
              <div class="quantity">
                <img
                  v-if="item.quantity === item.book.count"
                  src="../assets/images/arrow-up.png"
                  alt=""
                  @click="incrementQuantity(item)"
                  class="chg-quantity update-cart"
                  data-bs-toggle="modal"
                  data-bs-target="#demo"
                />
                <img
                  v-else
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
            <div
              v-if="getTotalDiscount"
              style="flex: 0.7"
              class="align-self-center ms-2"
            >
              <small v-if="item.book.discount != 0" class="text-success">
                {{
                  numberByCommas(
                    parseInt(
                      (item.book.price * item.book.discount * item.quantity) /
                        100
                    )
                  )
                }}- تومان
              </small>
            </div>
            <div style="flex: 1" class="align-self-center ms-2">
              {{
                numberByCommas(
                  item.quantity *
                    item.book.price *
                    (1 - item.book.discount / 100)
                )
              }}
              تومان
            </div>
            <div style="flex: 0.2" class="align-self-center">
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
              <h5 class="modal-title" id="exampleModalLabel">
                حذف از سبد خرید
              </h5>
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
              آیا از حذف این کتاب از سبد خرید خود اطمینان دارید؟
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
                @click="removeItem(item)"
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
    <div v-else class="d-flex flex-column">
      <div class="d-flex aligns-items-center justify-content-center empty-cart">
        <img src="../assets/images/empty-cart.png" alt="empty cart" />
      </div>
      <br />
      <div class="d-flex aligns-items-center justify-content-center">
        <h5>سبد خرید شما خالی می‌باشد</h5>
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
            <h5 class="modal-title" id="exampleModalLabel">تعداد محدود</h5>
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
            تنها همین تعداد از این کتاب موجود می‌باشد.
          </div>
          <div class="modal-footer">
            <button
              type="button"
              @click="logout()"
              class="btn btn-primary"
              data-bs-dismiss="modal"
            >
              تایید
            </button>
          </div>
        </div>
      </div>
    </div>
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
        total +=
          this.cart.items[i].quantity *
          this.cart.items[i].book.price *
          (1 - this.cart.items[i].book.discount / 100);
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
    incrementQuantity(item) {
      if (item.quantity < item.book.count) {
        item.quantity += 1;
      }
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

.empty-cart img {
  width: 200px;
  margin-top: 100px;
}
</style>
