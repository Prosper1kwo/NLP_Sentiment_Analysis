<?php
namespace Lib;

use GuzzleHttp;

class Amazon 
{
  public $common_params;

  private $access_key;
  private $secret_key;
  private $associate_tag;
  private $client;

  public function __construct($access_key, $secret_key, $associate_tag)
  {
    $this->access_key = $access_key;
    $this->secret_key = $secret_key;
    $this->associate_tag = $associate_tag;
    $this->common_params = [
      'Service' => 'AWSECommerceService',
      'Operation' => 'ItemSearch',
      'ResponseGroup' => 'Medium',
      'AssociateTag' => $associate_tag,
      'AWSAccessKeyId' => $access_key,
    ];
    $this->client = new GuzzleHttp\Client();
  }

  private function generateSignature($query)
  {
    ksort($query);

    $sign = http_build_query($query);

    $request_method = 'GET';
    $base_url = 'webservices.amazon.com';
    $endpoint = '/onca/xml';

    $string_to_sign = "{$request_method}\n{$base_url}\n{$endpoint}\n{$sign}";
    $signature = base64_encode(
        hash_hmac("sha256", $string_to_sign, $this->secret_key, true)
    );
    return $signature;
  }

  private function doRequest($query)
  {
    $timestamp = date('c');
    $query['Timestamp'] = $timestamp;
    $query = array_merge($this->common_params, $query);
    $query['Signature'] = $this->generateSignature($query);

    try {
      $response = $this->client->request(
        'GET', 'http://webservices.amazon.com/onca/xml', 
        ['query' => $query]
      );
      $contents = new \SimpleXMLElement($response->getBody()->getContents());
      return $contents;
    } catch (Exception $e) {
      return [
        'error' => $e->getMessage()
      ];
    }
  }

  public function getSearchIndices()
  {
    return [
      'All',
      'UnboxVideo',
      'Appliances',
      'MobileApps',
      'ArtsAndCrafts',
      'Automotive',
      'Books',
      'Music',
      'Wireless',
      'Collectibles',
      'PCHardware',
      'Electronics',
      'KindleStore',
      'Movies',
      'OfficeProducts',
      'Software',
      'Tools',
      'VideoGames'
    ];
  }

  public function itemSearch($keywords, $search_index)
  {
    $query = [
      'Keywords' => $keywords,
      'SearchIndex' => $search_index
    ];

    $response = $this->doRequest($query);
    return $response;
  }

}