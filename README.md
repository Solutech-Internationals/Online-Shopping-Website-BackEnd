# Online-Shopping-Website-BackEnd

## Setup Process

### 1. Install Scrapy

First, ensure that Scrapy is installed. If it's not installed, you can install it using `pip`.

```bash
pip install scrapy

```

### 2. Create a Virtual Environment


```bash
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
# On Windows
myenv\Scripts\activate
# On macOS/Linux
source myenv/bin/activate

# Install Scrapy in the virtual environment
pip install scrapy
```


### 3. Run the Spider

```bash
cd webscraper/webscraper/spiders/
scrapy runspider multi_spider.py -o output.json
```