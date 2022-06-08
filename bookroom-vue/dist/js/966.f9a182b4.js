"use strict";(self["webpackChunkbookroom_vue"]=self["webpackChunkbookroom_vue"]||[]).push([[966],{1966:function(t,l,o){o.r(l),o.d(l,{default:function(){return R}});var a=o(3396),u=o(7139);const s=(0,a._)("br",null,null,-1),r=(0,a._)("br",null,null,-1),i={class:"row"},n={class:"col-lg-3 col-md-6 mb-3"},e=["src","alt"],h=(0,a._)("br",null,null,-1),_=(0,a._)("br",null,null,-1),b={key:0},d=(0,a._)("span",null,"نویسنده: ",-1),k=(0,a._)("br",null,null,-1),g=(0,a._)("br",null,null,-1),c={key:1},m=(0,a._)("span",null,"مترجم: ",-1),p=(0,a._)("br",null,null,-1),w=(0,a._)("br",null,null,-1),v={key:2},y=(0,a._)("span",null,"تصویرگر: ",-1),f=(0,a._)("br",null,null,-1),q=(0,a._)("br",null,null,-1),z={key:3},$=(0,a._)("span",null,"ناشر: ",-1),D=(0,a._)("br",null,null,-1),B=(0,a._)("br",null,null,-1),C={class:"col-lg-9 col-md-6 mb-3"};function U(t,l,o,U,W,I){const L=(0,a.up)("router-link");return(0,a.wg)(),(0,a.iD)("div",null,[(0,a._)("h3",null,(0,u.zw)(W.book.name),1),s,r,(0,a._)("div",i,[(0,a._)("div",n,[(0,a._)("img",{src:W.book.get_image,class:"img-thumbnail",alt:W.book.name,width:"230"},null,8,e),h,_,W.author?((0,a.wg)(),(0,a.iD)("div",b,[d,(0,a.Wm)(L,{to:W.author_slug},{default:(0,a.w5)((()=>[(0,a.Uk)((0,u.zw)(W.author),1)])),_:1},8,["to"]),k,g])):(0,a.kq)("",!0),W.translator?((0,a.wg)(),(0,a.iD)("div",c,[m,(0,a.Wm)(L,{to:W.translator_slug},{default:(0,a.w5)((()=>[(0,a.Uk)((0,u.zw)(W.translator),1)])),_:1},8,["to"]),p,w])):(0,a.kq)("",!0),W.illustrator?((0,a.wg)(),(0,a.iD)("div",v,[y,(0,a.Wm)(L,{to:W.illustrator_slug},{default:(0,a.w5)((()=>[(0,a.Uk)((0,u.zw)(W.illustrator),1)])),_:1},8,["to"]),f,q])):(0,a.kq)("",!0),W.publisher?((0,a.wg)(),(0,a.iD)("div",z,[$,(0,a.Wm)(L,{to:W.publisher_slug},{default:(0,a.w5)((()=>[(0,a.Uk)((0,u.zw)(W.publisher),1)])),_:1},8,["to"])])):(0,a.kq)("",!0),D,(0,a._)("div",null,"سال نشر: "+(0,u.zw)(W.book.publish_year),1),B,(0,a._)("div",null,"تعداد صفحات: "+(0,u.zw)(W.book.page_count),1)]),(0,a._)("div",C,(0,u.zw)(W.book.description),1)])])}var W=o(6265),I=o.n(W),L={name:"Book",data(){return{book:{},author:"",author_slug:"",translator:"",translator_slug:"",illustrator:"",illustrator_slug:"",publisher:"",publisher_slug:""}},mounted(){this.getBook()},methods:{async getBook(){this.$store.commit("setIsLoading",!0);const t=this.$route.params.category_slug,l=this.$route.params.book_slug;await I().get(`/api/v1/books/${t}/${l}/`).then((t=>{this.book=t.data,t.data.author&&(this.author=t.data.author[0],this.author_slug=t.data.author[1]),t.data.translator&&(this.translator=t.data.translator[0],this.translator_slug=t.data.translator[1]),t.data.illustrator&&(this.illustrator=t.data.illustrator[0],this.illustrator_slug=t.data.illustrator[1]),t.data.publisher&&(this.publisher=t.data.publisher[0],this.publisher_slug=t.data.publisher[1]),document.title=this.book.name+" | BookRoom",console.log("publisher: ",this.publisher)})).catch((t=>console.log(t))),this.$store.commit("setIsLoading",!1)},addToCart(){(isNaN(this.quantity)||this.quantity<1)&&(this.quantity=1);const t={book:this.book,quantity:this.quantity};this.$store.commit("addToCart",t)}}},N=o(89);const T=(0,N.Z)(L,[["render",U]]);var R=T}}]);
//# sourceMappingURL=966.f9a182b4.js.map