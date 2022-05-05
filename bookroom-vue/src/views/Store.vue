<template>
  <div class="row">
    <BookBox v-for="book in bookList" :key="book.id" v-bind:book="book" />
  </div>
</template>

<script>
import axios from "axios";
import BookBox from "@/components/BookBox";

export default {
  name: "Store",
  data() {
    return {
      bookList: [],
      quantity: 1,
    };
  },

  components: { BookBox },
  mounted() {
    this.getBookList();
    document.title = "Home | BookRoom";
  },
  methods: {
    async getBookList() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/book_list/")
        .then((res) => {
          this.bookList = res.data;
        })
        .catch((err) => console.log(err));

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

<style scoped></style>
