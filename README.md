<h1> Study App</h1>
<h3> This was our project submission for <b>Hack The North 2020!</b> </h3>

<p> Our app allows the user to upload a .mp3 file and then input a "keyword". The video will then be transcribed into a script and then the timestamp associated with the word will then be outputted to the application.  </p>

<p> I created the Google Cloud Project, associated bucket and scripts to automatically upload files to the cloud and then have those videos transcribed </p>

<p> Additionally, I created the backend API was created using Django and Django Rest Framework to make API calls to Google Cloud, specifically the Google Speech to Text APIs and calls to upload the .mp3 file to a bucket in google cloud (if the file is longer than 1 minute long then google requires it to be placed in the bucket).</p>

<p> Here's a demo of how our project works!<p>
<video width="320" height="240" controls>
    <source src="devpost_submission.mp4" type="video/mp4">
</video>
<br>
<a href="https://i.vimeocdn.com/video/1037532301">Demo Link</a>
