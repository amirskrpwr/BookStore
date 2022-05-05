<template>
  <div>
    <h3>{{ book.name }}</h3>
    <div>{{ book.description }}</div>
    <img :src="book.get_image" :alt="book.name" />
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Book",
  data() {
    return {
      book: {},
    };
  },
  mounted() {
    this.getBook();
  },
  methods: {
    async getBook() {
      this.$store.commit("setIsLoading", true);

      const category_slug = this.$route.params.category_slug;
      const book_slug = this.$route.params.book_slug;

      await axios
        .get(`/api/v1/books/${category_slug}/${book_slug}/`)
        .then((res) => {
          this.book = res.data;
          document.title = this.book.name + " | BookRoom";
        })
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        book: this.book,
        quantity: this.quantity,
      };
      this.$store.commit("addToCart", item);
    },
  },
};
</script>

<style></style>
