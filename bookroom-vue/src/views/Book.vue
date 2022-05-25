<template>
  <div>
    <h3>{{ book.name }}</h3>
    <br /><br />
    <div class="row">
      <div class="col-lg-3 col-md-6 mb-3">
        <img :src="book.get_image" :alt="book.name" /><br /><br />
        <div v-if="author">
          <span>نویسنده: </span>
          <router-link :to="author_slug">{{ author }}</router-link>
          <br /><br />
        </div>

        <div v-if="translator">
          <span>مترجم: </span>
          <router-link :to="translator_slug">{{ translator }}</router-link>
          <br /><br />
        </div>

        <div v-if="publisher">
          <span>ناشر: </span>
          <router-link :to="publisher_slug">{{ publisher }}</router-link>
        </div>
        <br />
        <div>سال نشر: {{ book.publish_year }}</div>
        <br />
        <div>تعداد صفحات: {{ book.page_count }}</div>
      </div>
      <div class="col-lg-9 col-md-6 mb-3">{{ book.description }}</div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Book",
  data() {
    return {
      book: {},
      author: "",
      author_slug: "",
      translator: "",
      translator_slug: "",
      publisher: "",
      publisher_slug: "",
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

          if (res.data.author) {
            this.author = res.data.author[0];
            this.author_slug = res.data.author[1];
          }

          if (res.data.translator) {
            this.translator = res.data.translator[0];
            this.translator_slug = res.data.translator[1];
          }

          if (res.data.publisher) {
            this.publisher = res.data.publisher[0];
            this.publisher_slug = res.data.publisher[1];
          }

          document.title = this.book.name + " | BookRoom";

          console.log("publisher: ", this.publisher);
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
