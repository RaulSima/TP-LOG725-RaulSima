shader_type canvas_item;

//application de l'effet de l'exercice 2 et exercice 3 en meme temps

void vertex() {
	//c'est le meme effet que l'ex1 mais applique seulement sur la partie avant du sprite
	if(VERTEX.x > 0.0) {
		VERTEX = vec2(VERTEX.x + sin(TIME) * 10.0 , VERTEX.y - cos(TIME) * 10.0 );
	}
}

void fragment() {
// Apply a simple blur filter
    vec3 color = vec3(255, 0, 255);

    COLOR.rgb -= color;
}