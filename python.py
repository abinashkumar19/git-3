# ---------------- S3 Bucket ----------------
resource "aws_s3_bucket" "public_bucket" {
  bucket = "abinash-public-bucket-${random_integer.rand.result}"

  tags = {
    Name        = "PublicBucket"
    Environment = "test"
  }
}

resource "random_integer" "gand" {
  min = 10000
  max = 99999
}
