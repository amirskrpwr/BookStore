<template>
  <div>
    <div>
      <h1>{{ username }}</h1>
      <div v-if="email">
        <h3>{{ email }}</h3>
        <button class="btn btn-primary">Change Email</button>
      </div>
      <div v-else><button class="btn btn-warning">Add Email</button></div>
      <br />
      <div>
        <button
          class="btn btn-danger"
          data-bs-toggle="modal"
          data-bs-target="#demo"
        >
          Log out
        </button>
      </div>
    </div>
    <div v-show="orders.length">
      <hr />
      <h2>Orders</h2>
      <br />
      <div v-for="order in orders" :key="order.id">
        <div class="box-element">
          <div class="cart-row">
            <div style="flex: 1.5"></div>
            <div style="flex: 1.5"><strong>Item</strong></div>
            <div style="flex: 1"><strong>Price</strong></div>
            <div style="flex: 1"><strong>Quantity</strong></div>
            <div style="flex: 1"><strong>Total</strong></div>
          </div>
          <span></span>
          <div v-for="item in order.orderItems" :key="item.id" class="cart-row">
            <div style="flex: 1.5">
              <router-link :to="item.book.get_absolute_url">
                <img
                  :src="item.book.get_image"
                  :alt="item.book.name"
                  class="row-image"
                />
              </router-link>
            </div>
            <div style="flex: 1.5">
              <p>{{ item.book.name }}</p>
            </div>
            <div style="flex: 1">
              <p>${{ numberByCommas(parseInt(item.book.price)) }}</p>
            </div>
            <div style="flex: 1">
              <p>x{{ item.quantity }}</p>
            </div>
            <div style="flex: 1">
              <p>${{ numberByCommas(item.book.price * item.quantity) }}</p>
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
            <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">Do you want to log out?</div>
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
              @click="logout()"
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

      await axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/v1/users/me/",
        auth: {
          username: this.username,
          password: this.password,
        },
      })
        .then((res) => {
          this.id = res.data.id;
          this.email = res.data.email;
          console.log(res.data);
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
