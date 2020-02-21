 <template>
    <view class="status-bar" :style="{ backgroundColor: color }"></view>
 </template>

<script>
export default {
    props: ['color']    
}

</script>

 <<style>
.status-bar {
    height: 20px; 
}
 </style>