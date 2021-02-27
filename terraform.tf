resource "docker_image" "flask" {
  name         = "aldebaran1582/flask:latest"
  keep_locally = true
}
resource "docker_container" "flask" {
  image = docker_image.flask.latest
  name  = "bitwala-challenge"
  ports {
    internal = 443
    external = 443
  }
}