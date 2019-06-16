# atx-storage
Store images, videos and so on.

# API
上传文件

```bash
$ http POST $SERVER_URL/uploads file@upload.txt
{
	"urls": "http://localhost:5000/uploads/071d251339ff6ed6f5aa020d5aa0cd14/upload.txt"
}
```

File will be stored with the following structure

```
uploads
├── txt
     └── 071d251339ff6ed6f5aa020d5aa0cd14.raw
```

Download file

```bash
wget http://localhost:5000/uploads/071d251339ff6ed6f5aa020d5aa0cd14/upload.txt
# filename can change to other name, but download is the same file
wget http://localhost:5000/uploads/071d251339ff6ed6f5aa020d5aa0cd14/upload-other-name.txt
```

# LICENSE
[MIT](LICENSE)
