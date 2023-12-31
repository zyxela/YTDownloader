package com.example.youtubedownloader

import android.annotation.SuppressLint
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.ProgressBar
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModelProvider
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.Job
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.withContext

class MainActivity : AppCompatActivity() {
    private lateinit var progressBar: ProgressBar

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (!Python.isStarted()) Python.start(AndroidPlatform(this))
        val pythonObj = Python.getInstance()

        progressBar = findViewById<ProgressBar>(R.id.progressBar)
        val module = pythonObj.getModule("downloader")
        val viewModel = ViewModelProvider(this)[MainViewModel::class.java]
        GlobalScope.launch {
            viewModel.updateProgress(module)
        }
        viewModel.currentProgress.observe(this) {
            progressBar.progress = viewModel.currentProgress.value ?: 0
        }
        var file: Job? = null;
        findViewById<Button>(R.id.mp4).setOnClickListener {
            val link = findViewById<TextView>(R.id.tv_link).text.toString()
            Toast.makeText(this, "Start downloading", Toast.LENGTH_SHORT).show()
            try {
                GlobalScope.launch {

                    withContext(Dispatchers.Main) {
                        file = viewModel.startVideoDownloading(module, link)
                        Toast.makeText(it.context, "Downloaded", Toast.LENGTH_SHORT).show()
                    }
                }

            } catch (e: Exception) {
                Log.e("CONNECT", "${e.message}")
                Toast.makeText(this, "${e.cause}", Toast.LENGTH_LONG).show()
            }

        }
        findViewById<Button>(R.id.mp3).setOnClickListener {
            val link = findViewById<TextView>(R.id.tv_link).text.toString()
            try {
                Toast.makeText(this, "Start downloading", Toast.LENGTH_SHORT).show()
                GlobalScope.launch {
                    file  = viewModel.startAudioDownloading(module, link)
                    withContext(Dispatchers.Main) {
                        Toast.makeText(it.context, "Downloaded", Toast.LENGTH_SHORT).show()
                    }
                }
            } catch (e: Exception) {
                Toast.makeText(this, "${e.cause}", Toast.LENGTH_LONG).show()
                Log.i("e", e.message!!)
            }

        }

        findViewById<Button>(R.id.cancel).setOnClickListener {
            runBlocking {
                launch {
                    file?.cancel()
                    //file = null
                }
            }
        }

    }
}