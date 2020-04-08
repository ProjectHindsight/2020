<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">

        <h3>Hey!<br/>Can we ask you something?</h3>
        <hr>
        <h1>{{ questionData.question }}</h1>
        <br>
        <alert :message=info v-if="showInfo"></alert>

        <b-form @submit="onSubmit" class="w-100">
          <b-form-textarea id="textarea" v-model="answer"
                              placeholder="Give us your answer!"
                              rows="3" max-rows="6"
                              v-if="!showInfo">
            </b-form-textarea>
            <br>
          <b-button type="submit"
                    variant="primary"
                    :disabled="answer === ''"
                    v-if="!showInfo">
                      Submit
          </b-button>
        </b-form>

      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      questionData: {},
      answer: '',
      showInfo: false,
      info: '',
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getQuestion() {
      const path = 'http://localhost:5000/questions';
      axios.get(path)
        .then((res) => {
          const allQuestions = res.data.questions;
          const randomIndex = Math.floor(Math.random() * allQuestions.length);
          const randomQuestion = allQuestions[randomIndex];
          this.questionData = randomQuestion;
          console.log(this.questionData);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    initAnswerForm() {
      this.answer = '';
    },
    submitAnswer(payload) {
      const path = 'http://localhost:5000/user_entry';
      axios.post(path, payload)
        .then(() => {
          this.info = 'Thank you for your submission!';
          this.showInfo = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    onSubmit(event) {
      event.preventDefault();
      const payload = {
        answer: this.answer,
        questionId: this.questionData.id,
        sentOn: Date.now(),
        submittedOn: Date.now(),
        userId: 'user1',
      };
      console.log(payload);
      this.submitAnswer(payload);
      this.initAnswerForm();
    },
  },
  created() {
    this.getQuestion();
  },
};
</script>
