<template>
  <div class="preview">
    <h2>Prévia da Camisa</h2>
    <div v-if="shirt" :style="{ backgroundColor: color }" class="shirt-preview">
      <img :src="shirt.imageUrl" alt="Camisa" />
      <p>Estampa: {{ print }}</p>
    </div>
    <p v-else>Selecione uma camisa para ver a prévia.</p>
  </div>
</template>

<script>
export default {
  props: ['shirt', 'color', 'print']
};
</script>

<style>
.preview {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
  margin-top: 20px;
}

.preview h2 {
  font-size: 1.2em;
  margin-bottom: 10px;
}

.shirt-preview {
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.shirt-preview img {
  max-width: 100%;
  height: auto;
}

.shirt-preview p {
  font-size: 1em;
  margin-top: 10px;
}
</style>