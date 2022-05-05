import { createStore } from "vuex";

export default createStore({
    state: {
        cart: {
            items: [],
        },
        isAuthenticated: false,
        token: "",
        isLoading: false,
        username: "",
        password: "",
    },
    getters: {},
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem("cart")) {
                state.cart = JSON.parse(localStorage.getItem("cart"));
            } else {
                localStorage.setItem("cart", JSON.stringify(state.cart));
            }

            if (localStorage.getItem("token")) {
                state.token = localStorage.getItem("token");
                state.isAuthenticated = true;
                state.username = localStorage.getItem("username");
                state.password = localStorage.getItem("password");
            } else {
                state.token = "";
                state.isAuthenticated = false;
                state.username = "";
                state.password = "";
            }
        },

        resetStore(state) {
            state.cart = { items: [] };
            state.isAuthenticated = false;
            state.token = "";
            state.isLoading = false;
            username = "";
            password = "";

            localStorage.setItem("cart", JSON.stringify(state.cart));
            localStorage.setItem(
                "isAuthenticated",
                JSON.stringify(state.isAuthenticated)
            );
            localStorage.setItem("isLoading", JSON.stringify(state.isLoading));
            localStorage.setItem("token", state.token);
            localStorage.setItem("username", username);
            localStorage.setItem("password", password);
            console.log(state);
        },

        addToCart(state, item) {
            const exists = state.cart.items.filter((i) => i.book.id === item.book.id);
            if (exists.length) {
                exists[0].quantity =
                    parseInt(exists[0].quantity) + parseInt(item.quantity);
            } else {
                state.cart.items.push(item);
            }

            localStorage.setItem("cart", JSON.stringify(state.cart));
        },

        removeFromCart(state, item) {
            state.cart.items = state.cart.items.filter(
                (i) => i.book.id !== item.book.id
            );
            localStorage.setItem("cart", JSON.stringify(state.cart));
        },

        setIsLoading(state, status) {
            state.isLoading = status;
        },

        setToken(state, token) {
            state.token = token;
            state.isAuthenticated = true;
        },

        setUsername(state, username) {
            state.username = username;
        },

        setPassword(state, password) {
            state.password = password;
        },

        removeToken(state) {
            state.token = "";
            state.isAuthenticated = false;
            state.username = "";
            state.password = "";
        },
    },
    actions: {},
    modules: {},
});