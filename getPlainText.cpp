#include <iostream>
#include <string>
#include <curl/curl.h>

size_t WriteCallback(char *contents, size_t size, size_t nmemb, void *userp)
{
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

int main(int argc, char * argv[])
{
    curl_global_init(CURL_GLOBAL_ALL);

    CURL* easyhandle = curl_easy_init();
    std::string readBuffer;

    if (easyhandle) {
        curl_easy_setopt(easyhandle, CURLOPT_URL, "https://gnu.terminalroot.com.br/ip.php");
        curl_easy_setopt(easyhandle, CURLOPT_VERBOSE, 1L);
        curl_easy_setopt(easyhandle, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(easyhandle, CURLOPT_WRITEDATA, &readBuffer);

        curl_easy_perform(easyhandle);

        std::cout << readBuffer << std::endl;
    }
    return 0;
}
