<template>
  <div>
    <h2>{{ author.name }}</h2>
    <br />
    <img
      v-if="author.get_image"
      :src="author.get_image"
      class="img-thumbnail"
      width="200"
      height="150"
      :alt="author.name"
    />
    <img
      v-else
      src="../assets/images/default.png"
      class="img-thumbnail"
      width="200"
      height="150"
      :alt="author.name"
    />
    <br />
    <br />
    <div v-show="books.length" class="row">
      <h2>Books</h2>
      <BookBox v-for="book in books" :key="book.id" v-bind:book="book" />
    </div>
    <div v-show="translations.length" class="row">
      <h2>Translations</h2>
      <BookBox v-for="book in translations" :key="book.id" v-bind:book="book" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import BookBox from "@/components/BookBox.vue";

export default {
  name: "Author",
  data() {
    return {
      author: {},
      books: [],
      translations: [],
    };
  },
  mounted() {
    this.getAuthor();
  },
  methods: {
    async getAuthor() {
      this.$store.commit("setIsLoading", true);

      const author_slug = this.$route.params.author_slug;
      await axios
        .get(`/api/v1/authors/${author_slug}/`)
        .then((res) => {
          this.author = res.data;
          this.books = this.author.books;
          this.translations = this.author.translations;
          document.title = this.author.name + " | BookRoom";
        })
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
  },
  components: {
    BookBox,
  },
};
</script>

<style></style>
