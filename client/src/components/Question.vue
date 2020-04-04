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

<script src="./scripts/Question.js"/>
