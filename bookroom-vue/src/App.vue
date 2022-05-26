<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
      <div class="container">
        <router-link to="/" class="navbar-brand logo ms-2">
          <i class="fas fa-book"></i> کتابخانه
        </router-link>
        <div class="d-flex flex-row-reverse">
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
        </div>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto me-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/authors" class="nav-link active">
                نویسندگان
              </router-link>
            </li>
            <li class="nav-item">
              <router-link to="/publishers" class="nav-link active">
                ناشران
              </router-link>
            </li>
          </ul>
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/publishers" class="nav-link active">
                ناشران
              </router-link>
            </li>
            <li class="nav-item">
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
                      دسته‌بندی‌ها
                    </button>
                    <ul
                      class="dropdown-menu"
                      aria-labelledby="dropdownMenuButton1"
                    >
                      <li>
                        <router-link to="/" class="dropdown-item">
                          کتابخانه
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
            </li>
            <li class="nav-item">
              <form class="d-flex me-3" method="get" action="/search">
                <input
                  class="form-control ms-2"
                  type="search"
                  placeholder="جستجو"
                  aria-label="Search"
                  name="query"
                />
                <button class="btn btn-outline-success" type="submit">
                  جستجو
                </button>
              </form>
            </li>
          </ul>
          <div class="collapse navbar-collapse" id="navbarNav"></div>

          <div class="form-inline my-2 ms-2 my-lg-0">
            <div v-if="$store.state.isAuthenticated">
              <router-link class="btn btn-primary" to="/my-account">
                <strong>{{ $store.state.username }}</strong>
              </router-link>
            </div>
            <div v-else>
              <router-link class="btn btn-warning" to="/log-in">
                ورود
              </router-link>
            </div>
          </div>

          <router-link to="/cart" class="position-relative me-3"
            ><img src="@/assets/images/cart.png" alt="cart" id="cart-icon" />
            <span
              class="translate-middle position-absolute top-0 start-100 badge rounded-pill bg-warning"
            >
              {{ cartTotalLength }}
            </span>
          </router-link>
        </div>
      </div>
    </nav>

    <div
      v-bind:class="{ hidden: !$store.state.isLoading }"
      class="loader-container"
    >
      <img src="@/assets/images/loader-img.gif" alt="loader image" />
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

<style>
@font-face {
  font-family: "Vazir";
  src: url(@/assets/fonts/Vazir-Regular.ttf);
}
:root {
  --green: #27ae60;
  --dark-color: #219150;
  --black: #444;
  --light-color: #666;
  --border: 0.1rem solid rgba(0, 0, 0, 0.1);
  --border-hover: 0.1rem solid var(--black);
  --box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.1);
}

* {
  font-family: "Vazir";
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  outline: none;
  border: none;
  text-decoration: none;
  text-transform: capitalize;
  transition: all 0.2s linear;
  transition: width none;
}

html {
  overflow-x: hidden;
  scroll-padding-top: 5rem;
  scroll-behavior: smooth;
}

html::-webkit-scrollbar {
  width: 1rem;
}

html::-webkit-scrollbar-track {
  background: transparent;
}

html::-webkit-scrollbar-thumb {
  background: var(--black);
}

#cart-icon {
  width: 30px;
  display: inline-block;
  margin-left: 15px;
}

.logo {
  font-size: 1.8rem;
  font-weight: bolder;
  color: var(--black);
}

.logo i {
  color: var(--green);
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

.loader-container {
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  z-index: 10000;
  background: #f7f7f7;
  display: flex;
  align-items: center;
  justify-content: center;
}

.loader-container img {
  height: 10rem;
}
</style>
