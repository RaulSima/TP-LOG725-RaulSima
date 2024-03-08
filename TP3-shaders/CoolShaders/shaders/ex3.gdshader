shader_type canvas_item;

void fragment() {
// Apply a simple blur filter
    vec3 color = vec3(255, 0, 255);

    COLOR.rgb -= color;
}
