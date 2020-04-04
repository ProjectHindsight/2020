import axios from 'axios';
import Alert from '../Alert.vue';

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
