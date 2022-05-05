<template>
  <div>
    <h2>Search term: "{{ query }}"</h2>
    <div class="row">
      <BookBox v-for="book in books" :key="book.id" v-bind:book="book" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import BookBox from "@/components/BookBox.vue";

export default {
  name: "Search",
  components: {
    BookBox,
  },
  data() {
    return {
      books: [],
      query: "",
    };
  },
  mounted() {
    document.title = "Search | BookRoom";
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);

    if (params.get("query")) {
      this.query = params.get("query");
      this.performSearch();
    }
  },
  methods: {
    async performSearch() {
      this.$store.commit("setIsLoading", true);

      axios
        .post("api/v1/books/search", { query: this.query })
        .then((res) => {
          this.books = res.data;
        })
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

<style></style>
