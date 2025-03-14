<script setup lang="ts">
import { onMounted, ref } from 'vue'

const prices = ref([])

onMounted(async () => {
	const res = await fetch('http://127.0.0.1:8000/prices')
	const data = await res.json()
	prices.value = data.prices || [] // Access the 'prices' property from the response
	console.log(prices.value)
})
</script>

<template>
	<div>
		<h1>Toy Prices</h1>
		<ul>
			<li v-for="price in prices" :key="price">
				{{ price }}
			</li>
		</ul>
	</div>
</template>
