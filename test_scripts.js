import http from 'k6/http';
import {check, sleep} from 'k6';

export let options = {
  stages: [
    { duration: '5s', target: 100 },
    { duration: '10s', target: 100 },
  ]
};

export default function () {
  let res = http.get('http://localhost:8001/requests_api');
  // let res = http.get('http://localhost:8001/aiohttp_api');
  check(res, {
   'is status 200': (r) => r.status === 200,
 })
  sleep(0.1);
}