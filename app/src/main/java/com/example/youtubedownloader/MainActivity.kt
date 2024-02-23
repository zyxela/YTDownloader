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
import androidx.lifecycle.lifecycleScope
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {
    private lateinit var progressBar: ProgressBar
    private lateinit var viewModel: MainViewModel


    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (!Python.isStarted()) Python.start(AndroidPlatform(this))
        val pythonObj = Python.getInstance()

        val textBox = findViewById<TextView>(R.id.tv_link)

        progressBar = findViewById(R.id.progressBar)
        val module = pythonObj.getModule("downloader")
        viewModel = ViewModelProvider(this)[MainViewModel::class.java]


        viewModel.updateProgress(module)



        lifecycleScope.launch {
            viewModel.currentProgress.collect { progress ->
                progressBar.progress = progress
            }

        }

        findViewById<Button>(R.id.mp4).setOnClickListener {
            val link = textBox.text.toString()
            Toast.makeText(this, "Start downloading", Toast.LENGTH_SHORT).show()
            try {
                viewModel.startVideoDownloading(module, link)
                Toast.makeText(it.context, "Downloaded", Toast.LENGTH_SHORT).show()
                // viewModel.cancelProgress()

            } catch (e: Exception) {
                Log.e("CONNECT", "${e.message}")
                Toast.makeText(this, "${e.cause}", Toast.LENGTH_LONG).show()
            }

        }
        findViewById<Button>(R.id.mp3).setOnClickListener {
            val link = textBox.text.toString()
            try {
                Toast.makeText(this, "Start downloading", Toast.LENGTH_SHORT).show()
                viewModel.startAudioDownloading(module, link)
                //viewModel.cancelProgress()
            } catch (e: Exception) {
                Toast.makeText(this, "${e.cause}", Toast.LENGTH_LONG).show()
                Log.i("e", e.message!!)
            }
        }

        findViewById<Button>(R.id.clear_link).setOnClickListener {
            textBox.text = ""
        }

    }
}