# YT-Mp3-using-RapidApi
# YouTube to MP3 Converter API

A simple API service that converts YouTube videos to MP3 format. This API is deployed on Vercel and provides an easy way to get downloadable MP3 links from YouTube video IDs.

## API Reference

### Convert YouTube Video to MP3

```http
GET /convert?id={youtube_video_id}
```

#### Parameters

| Parameter | Type     | Description                                   |
|-----------|----------|-----------------------------------------------|
| `id`      | `string` | **Required**. YouTube video ID (e.g., mpxEUex3dek) |

#### Response Format

```json
{
  "duration": 171.80739095229,
  "filesize": 2624420,
  "link": "string",
  "msg": "success",
  "progress": 100,
  "status": "ok",
  "title": "string"
}
```

#### Response Fields

- `duration`: Length of the audio in seconds
- `filesize`: Size of the MP3 file in bytes
- `link`: Direct download link for the MP3 file
- `msg`: Status message
- `progress`: Conversion progress (100 when complete)
- `status`: Status of the request ("ok" for successful conversion)
- `title`: Original YouTube video title

## Example Usage

```bash
curl "https://yt-mp3-using-rapid-api.vercel.app/convert?id=mpxEUex3dek"
```

Example Response:
```json
{
  "duration": 171.80739095229,
  "filesize": 2624420,
  "link": "https://epsilon.123tokyo.xyz/get.php/5/a9/mpxEUex3dek.mp3?cid=MmEwMTo0Zjg6YzAxMjozMmVlOjoxfE5BfERF&h=dCyl7oKGl92yM4ueHz1CvQ&s=1738230722&n=JVKE%20-%20her%20%28Official%20Illustrated%20Music%20Video%29&uT=R&uN=YWF5ZXNoYW1haHRv",
  "msg": "success",
  "progress": 100,
  "status": "ok",
  "title": "JVKE - her (Official Illustrated Music Video)"
}
```

## Deployment

This API is deployed on Vercel. You can access it at:
```
https://yt-mp3-using-rapid-api.vercel.app
```

## Important Notes

- This API is for educational purposes only
- Please ensure you have the right to download and convert the videos
- The API might have rate limits and usage restrictions
- Download links are temporary and may expire after some time

## Error Handling

The API returns appropriate error messages when:
- Invalid video ID is provided
- Video is not available
- Conversion fails
- Rate limits are exceeded

