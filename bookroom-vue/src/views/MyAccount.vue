<template>
  <div>
    <h1>My Account</h1>
    <br />
    <div>id: {{ id }}</div>
    <div>email: {{ email }}</div>
    <div>{{ orders }}</div>
    <br />
    <div><button @click="logout()" class="btn btn-danger">Log out</button></div>
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
  },
};
</script>

<style></style>
