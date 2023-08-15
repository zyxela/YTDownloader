package com.example.youtubedownloader

import android.annotation.SuppressLint
import android.os.Bundle
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {
    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (!Python.isStarted()) Python.start(AndroidPlatform(this))

        val pythonObj = Python.getInstance()
        val module = pythonObj.getModule("downloader")

        findViewById<Button>(R.id.mp4).setOnClickListener {
            val link = "https://www.youtube.com/watch?v=aQNrG7ag2G4"
            GlobalScope.launch {
                module.callAttr(
                    "download", link,
                    filesDir.absolutePath
                )

            }

        }

        findViewById<Button>(R.id.mp3).setOnClickListener {
            GlobalScope.launch {
                module.callAttr(
                    "convertToAudio", filesDir.absolutePath
                )
            }
        }


    }
}