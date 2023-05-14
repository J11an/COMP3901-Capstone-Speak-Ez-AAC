<script>
    import WordPictureTile from './WordPictureTile.vue';

    export default {
        name:"WordDisplay",
        components: {WordPictureTile},

        data(){
            return{
                csrf_token:'',
                columns: [],
                newWord: '',
                newCategory: '',
                newSymbol: ''
            }
        },

        mounted(){
            this.fetchInitColumns().then((columns) => (this.columns = columns));
        },
        created() {
            this.getCsrfToken();
        },

        methods: {
            fetchInitColumns() {
                return fetch("api/inital_tree_setting", {
                    method: "GET",
                })
                    .then(function (response) {
                    return response.json();
                    })
                    .then(function (data) {
                    return data;
                    })
                    .catch(function (error) {
                    console.log(error);
                    return error;
                    });
            },

            addWord() {
                const formData = {
                    word: this.newWord,
                    category: this.newCategory,
                    symbol: this.newSymbol
                };

                console.log(formData)

                fetch("api/word", {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-CSRFToken": this.csrf_token,
                    },
                })
                .then(function (response) {
                    console.log(response)
                })
                .then(function (data) {
                    console.log(data)
                })
                .catch(error => {
                console.error("Error adding word:", error);
                });
            },

            test(){
                console.log("click")
            },

            getCsrfToken() {
                let self = this;
                fetch("/api/csrf-token")
                    .then((response) => response.json())
                    .then((data) => {
                    console.log(data);
                    self.csrf_token = data.csrf_token;
                    });
                },
            
        },  

    }
</script>

<template>
    <br/>
    <form @submit.prevent="addWord">
      <label for="word">Word:</label>
      <input type="text" id="word" v-model="newWord">

      <label for="category">Category:</label>
      <input type="text" id="category" v-model="newCategory">

      <label for="symbol">Symbol:</label>
      <input type="text" id="symbol" v-model="newSymbol">

      <button type="submit">Add Word</button>
    </form>
    <br/>
    <!-- <div v-for="column in this.columns">  
        <div v-for="word in column[1]" @draggable="true">
        <WordPictureTile
            :id="word.id"
            :word="word.word"
            :symbol="word.symbol"
            @click="test()"
        />
        </div> 
    </div> -->
    
</template>

<style>
</style>