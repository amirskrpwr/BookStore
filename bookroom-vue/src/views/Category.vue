<template>
  <div class="row">
    <BookBox v-for="book in category.books" :key="book.id" v-bind:book="book" />
  </div>
</template>

<script>
import axios from "axios";
import BookBox from "@/components/BookBox";

export default {
  name: "Category",
  data() {
    return {
      category: {
        books: [],
      },
    };
  },
  mounted() {
    this.getCategory();
  },
  watch: {
    $route(to, from) {
      if (to.name == "Category") {
        this.getCategory();
      }
    },
  },
  components: { BookBox },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug;

      this.$store.commit("setIsLoading", true);

      await axios
        .get(`api/v1/books/${categorySlug}/`)
        .then((res) => {
          this.category = res.data;
          document.title = this.category.name + " | BookRoom";
        })
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

<style scoped></style>
