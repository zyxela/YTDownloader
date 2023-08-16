package com.example.youtubedownloader

import android.annotation.SuppressLint
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import android.widget.Toast
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
            val link = findViewById<TextView>(R.id.tv_link).text.toString()
            Toast.makeText(this, "Start downloading", Toast.LENGTH_SHORT).show()

            try {
                module.callAttr(
                    "download", link,
                    filesDir.absolutePath
                )
                Toast.makeText(this, "Downloaded", Toast.LENGTH_SHORT).show()

            } catch (e: Exception) {
                Toast.makeText(this, "INCORRECT LINK", Toast.LENGTH_LONG).show()
            }

        }

        findViewById<Button>(R.id.mp3).setOnClickListener {
            val link = findViewById<TextView>(R.id.tv_link).text.toString()
            GlobalScope.launch {
                module.callAttr(
                    "convertToAudio", link, filesDir.absolutePath
                )
            }
        }


    }
}