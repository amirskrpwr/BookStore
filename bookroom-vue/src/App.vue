<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <div class="container">
        <router-link to="/" class="navbar-brand">BookRoom</router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/authors" class="nav-link active">
              Authors
            </router-link>
          </li>
        </ul>
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link to="/publishers" class="nav-link active">
              Publishers
            </router-link>
          </li>
        </ul>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item ms-2">
                <div class="dropdown">
                  <button
                    class="btn dropdown-toggle"
                    type="button"
                    id="dropdownMenuButton1"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Categories
                  </button>
                  <ul
                    class="dropdown-menu"
                    aria-labelledby="dropdownMenuButton1"
                  >
                    <li>
                      <router-link to="/" class="dropdown-item">
                        Store
                      </router-link>
                    </li>
                    <li><hr class="dropdown-divider" /></li>
                    <li
                      v-for="category in categoryList"
                      v-bind:key="category.id"
                    >
                      <router-link
                        :to="category.get_absolute_url"
                        class="dropdown-item"
                        >{{ category.name }}</router-link
                      >
                    </li>
                  </ul>
                </div>
              </li>
            </ul>
            <form class="d-flex ms-3" method="get" action="/search">
              <input
                class="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
                name="query"
              />
              <button class="btn btn-outline-success" type="submit">
                Search
              </button>
            </form>
          </div>

          <div class="form-inline my-2 ms-2 my-lg-0">
            <div v-if="$store.state.isAuthenticated">
              <router-link class="btn btn-primary" to="/my-account">
                My Account
              </router-link>
              <span class="ms-4 me-3"
                ><strong>{{ $store.state.username }}</strong></span
              >
            </div>
            <div v-else>
              <router-link class="btn btn-warning" to="/log-in">
                Login
              </router-link>
            </div>
          </div>

          <router-link to="/cart"
            ><img src="@/assets/images/cart.png" alt="cart" id="cart-icon" />
            <span class="translate-middle badge rounded-pill bg-warning">
              {{ cartTotalLength }}
            </span>
          </router-link>
        </div>
      </div>
    </nav>

    <div
      class="d-flex justify-content-center margin-loading"
      v-bind:class="{ hidden: !$store.state.isLoading }"
    >
      <div class="spinner-border text-primary spinner-size" role="status">
        <span class="sr-only"></span>
      </div>
    </div>

    <section class="container p-5 margin-top">
      <router-view />
    </section>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      categoryList: [],
      cart: {
        items: [],
      },
      token: "",
      userInfo: {
        username: "",
        email: "",
      },
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
    // this.$store.commit("resetStore");

    const token = this.$store.state.token;

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },

  mounted() {
    this.cart = this.$store.state.cart;
    this.getCategoryList();
    console.log("category list: ", this.categoryList);
  },

  computed: {
    cartTotalLength() {
      let totalLength = 0;
      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
      }
      return totalLength;
    },
  },

  methods: {
    getCategoryList() {
      axios
        .get("/api/v1/category_list/")
        .then((res) => {
          this.categoryList = res.data;
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>

<style scoped>
#cart-icon {
  width: 30px;
  display: inline-block;
  margin-left: 15px;
}

.hidden {
  display: none !important;
}
.spinner-size {
  width: 4rem;
  height: 4rem;
}
.margin-top {
  margin-top: 40px;
}
.margin-loading {
  margin-top: 120px;
}
</style>
