shader_type canvas_item;

void vertex() {
	//c'est le meme effet que l'ex1 mais applique seulement sur la partie avant du sprite
	if(VERTEX.x > 0.0) {
		VERTEX = vec2(VERTEX.x + sin(TIME) * 10.0 , VERTEX.y - cos(TIME) * 10.0 );
	}
}