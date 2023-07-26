#!/usr/bin/node
// script that computes the number of tasks completed by user id

const request = require('request');

function CompletedTasks (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode === 200) {
        const todos = JSON.parse(body);

        const completedTasks = {};

        todos.forEach((todo) => {
          if (todo.completed) {
            if (!completedTasks[todo.userId]) {
              completedTasks[todo.userId] = 1;
            } else {
              completedTasks[todo.userId]++;
            }
          }
        });

        console.log(completedTasks);
      } else {
        console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
      }
    }
  });
}

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL.');
} else {
  CompletedTasks(apiUrl);
}
