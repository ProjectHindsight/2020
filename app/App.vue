<template>
  <view class="container">
    <StatusBar color="#00FF00"/>
    <Header title="2020"/>

    <view class="inputContainer">
      <text-input class="input" v-model="itemText"/>
      <touchable-opacity class="addBtn" :on-press="newInput"> 
        <text class="btnText">Add</text>
      </touchable-opacity>
    </view>

    <view class="item" v-for="item in items" :key="item.id">
      <touchable-opacity :on-press="() => toggle(item.id)">
        <text class="item-text done" v-if="item.done">{{ item.title }}</text>
        <text class="item-text" v-else>{{ item.title }}</text>
      </touchable-opacity>
      <touchable-opacity class="remove-btn" :on-press="() => remove(item.id)">
        <text class="remove-btn-text">Remove</text>
      </touchable-opacity>
    </view>
  </view>
</template>

<script>
import StatusBar from './components/status-bar';
import Header from './components/header';

export default {
  data() {
    return {
      itemText: '',
      count: 0,
      items: []
    }
  },
  components: {
    StatusBar,
    Header
  },
  methods: {
    newInput() {
      if (this.itemText != '') {
        this.items.push({
        id: this.count + 1,
        title: this.itemText,
        done: false
      })
      this.count++;
      this.itemText = '';
      }
    },
    toggle(id) {
      this.items = this.items.map(item => {
        if (item.id == id) item.done = !item.done;
        return item;
      })
    },
    remove(id) {
      this.items = this.items.filter(item => item.id !== id);
    }
  }
}
</script>
<style>
.container {
  background-color: white;
  flex: 1;
}
.inputContainer {
   flex-direction: row;
   justify-content: center;
   align-items: stretch;
}
.input {
  flex: 1;
  height: 35px;
  background-color: lightgray;
  font-size: 18px;
  color: #888888;
}
.addBtn {
  width: 100px;
  height: 35px;
  background-color: #FFCE00;
  justify-content: center;
  align-items: center;
}
.btnText {
   font-size: 18px;
   font-weight: 700;
}
.item {
  flex-direction: row;
  justify-content: space-between;
  padding: 15px;
} 
.item-text {
  font-size: 18px;
}
.done {
  color: #AAAAAA;
}
.remove-btn-text {
  font-size: 18px;
  color: red;
}

</style>
