#include <stdio.h>
#include <curl/curl.h>

// Callback function for handling data received by libcurl
size_t write_callback(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t total_size = size * nmemb;
    // Write the received data to stdout
    fwrite(contents, size, nmemb, stdout);
    return total_size;
}

int main(void) {
    // Initialize a CURL session
    CURL *curl = curl_easy_init();
    if (curl) {
        // Set the URL to fetch
        curl_easy_setopt(curl, CURLOPT_URL, "https://www.gov.uk/");
        // Set the write callback function to handle the data
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
        
        // Perform the request, capturing any errors
        CURLcode res = curl_easy_perform(curl);
        if (res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n",
                    curl_easy_strerror(res));
        }
        
        // Cleanup the CURL session
        curl_easy_cleanup(curl);
    } else {
        fprintf(stderr, "Failed to initialize CURL.\n");
    }
    return 0;
}