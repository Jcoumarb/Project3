import React from "react";
import { createRoot } from "react-dom/client";

async function fetchFilmData() {
	try {
		const filmId = window.location.pathname.split("/").pop();
		const response = await fetch(`/api/v1/film/${filmId}`);
		if (!response.ok) {
			throw new Error("Failed to fetch film data");
		}
		return await response.json();
	} catch (error) {
		console.error(error);
		return null;
	}
}
async function main() {
	const filmData = await fetchFilmData();


	const rootElt = document.getElementById("app");
	const root = createRoot(rootElt);
	root.render(
		<div>
			<h1>{filmData.title}</h1>
			<p>{filmData.description}</p>
			<a href="/">Back to List View</a>
		</div>
	);
}

window.onload=main
