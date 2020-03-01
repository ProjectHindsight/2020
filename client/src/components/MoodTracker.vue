<template>
<div>
    <div class="container">
        <div class="row">
            <div class="col-md-12">How are you feeling right now?</div>
        </div>
        <div>
    <div class="mt-3">
        <b-button-group>
        <b-button variant="danger">Very Bad</b-button>
        <b-button variant="warning">Bad</b-button>
        <b-button variant="info">Good</b-button>
        <b-button variant="success">Very Good</b-button>
        </b-button-group>
    </div>
</div>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
