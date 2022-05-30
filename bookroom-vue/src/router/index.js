import { createRouter, createWebHistory } from "vue-router";
import Store from "../views/Store.vue";
import store from "../store";

const routes = [{
        path: "/",
        name: "store",
        component: Store,
    },
    {
        path: "/about",
        name: "about",
        component: () =>
            import ("../views/About.vue"),
    },
    {
        path: "/cart",
        name: "cart",
        component: () =>
            import ("../views/Cart.vue"),
    },
    {
        path: "/cart/checkout",
        name: "checkout",
        component: () =>
            import ("../views/Checkout.vue"),
        meta: { requireLogin: true },
    },
    {
        path: "/:category_slug/",
        name: "Category",
        component: () =>
            import ("../views/Category.vue"),
    },
    {
        path: "/:category_slug/:book_slug/",
        name: "Book",
        component: () =>
            import ("../views/Book.vue"),
    },
    {
        path: "/search",
        name: "Search",
        component: () =>
            import ("../views/Search.vue"),
    },
    {
        path: "/sign-up",
        name: "SignUp",
        component: () =>
            import ("../views/SignUp.vue"),
    },
    {
        path: "/log-in",
        name: "Login",
        component: () =>
            import ("../views/Login.vue"),
    },
    {
        path: "/my-account",
        name: "MyAccount",
        component: () =>
            import ("../views/MyAccount.vue"),
        meta: { requireLogin: true },
    },
    {
        path: "/cart/success",
        name: "Success",
        component: () =>
            import ("../views/Success.vue"),
        meta: { requireLogin: true },
    },
    {
        path: "/authors",
        name: "AuthorList",
        component: () =>
            import ("../views/AuthorList.vue"),
    },
    {
        path: "/authors/:author_slug/",
        name: "Author",
        component: () =>
            import ("../views/Author.vue"),
    },
    {
        path: "/publishers",
        name: "PublisherList",
        component: () =>
            import ("../views/PublisherList.vue"),
    },
    {
        path: "/publishers/:publisher_slug/",
        name: "Publisher",
        component: () =>
            import ("../views/Publisher.vue"),
    },
    {
        path: "/illustrators",
        name: "IllustratorList",
        component: () =>
            import ("../views/IllustratorList.vue"),
    },
    {
        path: "/illustrators/:illustrator_slug/",
        name: "Illustrator",
        component: () =>
            import ("../views/Illustrator.vue"),
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

router.beforeEach((to, from, next) => {
    if (
        to.matched.some((record) => record.meta.requireLogin) &&
        !store.state.isAuthenticated
    ) {
        next({ name: "Login", query: { to: to.path } });
    } else {
        next();
    }
});

export default router;