from rest_framework.decorators import api_view
from rest_framework.response import Response

from google.cloud import storage
from google.cloud import speech
import json
import time

BUCKET_NAME = "staging.hack-the-north-301905.appspot.com"


# Create your views here.

@api_view(["GET"])
def create_object(request, format=None):
    if request.method == 'GET':
        storage_client = storage.Client.from_service_account_json(
            'C:\\Users\\Aman\\PycharmProjects\\study-app\\Hack The North-b2580a2a5f87.json'
        )

        # print(buckets = list(storage_client.list_buckets())
        bucket = storage_client.get_bucket(BUCKET_NAME)
        blob = bucket.blob("new music")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body["object"]["file"]
        # blob.upload_from_filename("C:\\Users\\Aman\\PycharmProjects\\study-app\\Ed Sheeran - Shape of You.mp3")
        blob.upload_from_filename(content)
    return Response(request.body.decode('utf-8'))


@api_view(['GET', 'POST', 'DELETE'])
def object_detail(request, format=None):
    if request.method == 'GET':
        storage_client = storage.Client.from_service_account_json(
            'C:\\Users\\Aman\\PycharmProjects\\study-app\\Hack The North-b2580a2a5f87.json'
        )

        # print(buckets = list(storage_client.list_buckets())
        bucket = storage_client.get_bucket(BUCKET_NAME)
        blob = bucket.blob("new music")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body["object"]["file"]
        # blob.upload_from_filename("C:\\Users\\Aman\\PycharmProjects\\study-app\\Ed Sheeran - Shape of You.mp3")
        blob.upload_from_filename(content)
        # return blob.public_url

        time.sleep(10)
        client = speech.SpeechClient.from_service_account_json(
            'C:\\Users\\Aman\\PycharmProjects\\study-app\\Hack The North-b2580a2a5f87.json'
        )

        audio = speech.RecognitionAudio(uri="gs://staging.hack-the-north-301905.appspot.com/new music")
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
            sample_rate_hertz=16000,
            language_code="en-US",
            enable_word_time_offsets=True,
        )

        operation = client.long_running_recognize(config=config, audio=audio)

        print("Allow time for operation to complete")
        result = operation.result(timeout=300)
        list = []

        for result in result.results:
            alternative = result.alternatives[0]
            print("Transcript: {}".format(alternative.transcript))
            print("Confidence: {}".format(alternative.confidence))

            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time
                end_time = word_info.end_time
                list.append([word, start_time.total_seconds(), end_time.total_seconds()])
                print(
                    f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}"
                )
                print(list)
        json_data = json.dumps(list)

        return Response(json_data)
