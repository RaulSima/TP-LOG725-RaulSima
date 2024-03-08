shader_type canvas_item;

void vertex() {
	// ceci est un changement des coord x et y mais ce n'est pas exactement le meme effet demande
	VERTEX = vec2(VERTEX.x + sin(TIME) * 10.0 , VERTEX.y - cos(TIME) * 10.0 );
}