#include <curl/curl.h>
#include <jansson.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure to hold the HTTP response
typedef struct {
    char *data;
    size_t size;
} HttpResponse;

// Callback function for libcurl to write response data
size_t write_callback(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t total_size = size * nmemb;
    HttpResponse *response = (HttpResponse *)userp;

    char *ptr = realloc(response->data, response->size + total_size + 1);
    if (ptr == NULL) {
        printf("Failed to allocate memory.\n");
        return 0;
    }

    response->data = ptr;
    memcpy(&(response->data[response->size]), contents, total_size);
    response->size += total_size;
    response->data[response->size] = '\0';

    return total_size;
}

int main() {
    CURL *curl;
    CURLcode res;

    HttpResponse response;
    response.data = malloc(1); // Initial allocation
    response.size = 0;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if (curl) {
        // Set the URL for the HTTP request
        curl_easy_setopt(curl, CURLOPT_URL, "https://www.go4schools.com/");

        // Set the callback function to handle the response
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&response);

        // Perform the HTTP request
        res = curl_easy_perform(curl);

        if (res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        } else {
            // Parse the JSON response using jansson
            json_error_t error;
            json_t *root = json_loads(response.data, 0, &error);

            if (!root) {
                fprintf(stderr, "JSON parsing error: %s\n", error.text);
            } else {
                // Extract and print specific fields from the JSON
                const char *title = json_string_value(json_object_get(root, "title"));
                int id = json_integer_value(json_object_get(root, "id"));

                printf("ID: %d\n", id);
                printf("Title: %s\n", title);

                json_decref(root);
            }
        }

        // Cleanup
        curl_easy_cleanup(curl);
    }

    free(response.data);
    curl_global_cleanup();

    return 0;
}