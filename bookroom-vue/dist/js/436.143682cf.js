"use strict";(self["webpackChunkbookroom_vue"]=self["webpackChunkbookroom_vue"]||[]).push([[436],{2436:function(l,t,o){o.r(t),o.d(t,{default:function(){return Z}});var r=o(3396),i=o(7139),s=o(9242),u=o(5865);const n=(0,r._)("br",null,null,-1),a={class:"row"},e={class:"col-lg-3 col-md-6 mb-3"},c=["src","alt"],d=["alt"],m={key:2},g=(0,r._)("br",null,null,-1),h={key:3},b=(0,r._)("br",null,null,-1),_={class:"col-lg-9 col-md-6 mb-3"},k={key:0},w=(0,r._)("br",null,null,-1),v=(0,r._)("br",null,null,-1),p=(0,r._)("br",null,null,-1),f=(0,r._)("br",null,null,-1),y={class:"row"},D=(0,r._)("h2",null,"کتاب‌ها",-1),B=(0,r._)("hr",null,null,-1);function z(l,t,o,z,I,$){const q=(0,r.up)("BookBox");return(0,r.wg)(),(0,r.iD)("div",null,[(0,r._)("h2",null,(0,i.zw)(I.illustrator.name),1),n,(0,r._)("div",a,[(0,r._)("div",e,[I.illustrator.get_image?((0,r.wg)(),(0,r.iD)("img",{key:0,src:I.illustrator.get_image,class:"img-thumbnail",width:"200",height:"150",alt:I.illustrator.name},null,8,c)):((0,r.wg)(),(0,r.iD)("img",{key:1,src:u,class:"img-thumbnail",width:"230",alt:I.illustrator.name},null,8,d)),I.illustrator.birth_date?((0,r.wg)(),(0,r.iD)("div",m,[g,(0,r._)("div",null,"تاریخ تولد: "+(0,i.zw)(I.illustrator.birth_date),1)])):(0,r.kq)("",!0),I.illustrator.birth_place?((0,r.wg)(),(0,r.iD)("div",h,[b,(0,r._)("div",null,"محل تولد: "+(0,i.zw)(I.illustrator.birth_place),1)])):(0,r.kq)("",!0)]),(0,r._)("div",_,[I.illustrator.introduction?((0,r.wg)(),(0,r.iD)("div",k,[(0,r._)("p",null,(0,i.zw)(I.illustrator.introduction),1),w,v])):(0,r.kq)("",!0)])]),p,f,(0,r.wy)((0,r._)("div",y,[D,B,((0,r.wg)(!0),(0,r.iD)(r.HY,null,(0,r.Ko)(I.books,(l=>((0,r.wg)(),(0,r.j4)(q,{key:l.id,book:l},null,8,["book"])))),128))],512),[[s.F8,I.books.length]])])}var I=o(6265),$=o.n(I),q=o(9169),x={name:"illustrator",data(){return{illustrator:{},books:[]}},mounted(){this.getIllustrator()},methods:{async getIllustrator(){this.$store.commit("setIsLoading",!0);const l=this.$route.params.illustrator_slug;await $().get(`/api/v1/illustrators/${l}/`).then((l=>{this.illustrator=l.data,this.books=this.illustrator.books,document.title=this.illustrator.name+" | BookRoom"})).catch((l=>console.log(l))),this.$store.commit("setIsLoading",!1)}},components:{BookBox:q.Z}},C=o(89);const L=(0,C.Z)(x,[["render",z]]);var Z=L},5865:function(l,t,o){l.exports=o.p+"img/default.95adfc54.png"}}]);
//# sourceMappingURL=436.143682cf.js.map